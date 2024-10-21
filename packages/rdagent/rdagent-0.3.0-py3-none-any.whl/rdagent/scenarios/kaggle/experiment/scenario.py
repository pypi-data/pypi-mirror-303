import io
import json
import pickle
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
from jinja2 import Environment, StrictUndefined

from rdagent.app.kaggle.conf import KAGGLE_IMPLEMENT_SETTING
from rdagent.core.experiment import Task
from rdagent.core.prompts import Prompts
from rdagent.core.scenario import Scenario
from rdagent.oai.llm_utils import APIBackend
from rdagent.scenarios.kaggle.experiment.kaggle_experiment import KGFactorExperiment
from rdagent.scenarios.kaggle.kaggle_crawler import (
    crawl_descriptions,
    leaderboard_scores,
)
from rdagent.scenarios.kaggle.knowledge_management.vector_base import (
    KaggleExperienceBase,
)

prompt_dict = Prompts(file_path=Path(__file__).parent / "prompts.yaml")

KG_ACTION_FEATURE_PROCESSING = "Feature processing"
KG_ACTION_FEATURE_ENGINEERING = "Feature engineering"
KG_ACTION_MODEL_FEATURE_SELECTION = "Model feature selection"
KG_ACTION_MODEL_TUNING = "Model tuning"
KG_ACTION_LIST = [
    KG_ACTION_FEATURE_PROCESSING,
    KG_ACTION_FEATURE_ENGINEERING,
    KG_ACTION_MODEL_FEATURE_SELECTION,
    KG_ACTION_MODEL_TUNING,
]


class KGScenario(Scenario):
    def __init__(self, competition: str) -> None:
        super().__init__()
        self.competition = competition
        self.competition_descriptions = crawl_descriptions(competition)
        self.input_shape = None
        self._source_data = self.source_data

        self.competition_type = None
        self.competition_description = None
        self.target_description = None
        self.competition_features = None
        self.submission_specifications = None
        self.model_output_channel = None
        self.evaluation_desc = None
        self.leaderboard = leaderboard_scores(competition)
        self.evaluation_metric_direction = float(self.leaderboard[0]) > float(self.leaderboard[-1])
        self.vector_base = None
        self.mini_case = KAGGLE_IMPLEMENT_SETTING.mini_case
        self._analysis_competition_description()
        self.if_action_choosing_based_on_UCB = KAGGLE_IMPLEMENT_SETTING.if_action_choosing_based_on_UCB
        self.if_using_graph_rag = KAGGLE_IMPLEMENT_SETTING.if_using_graph_rag
        self.if_using_vector_rag = KAGGLE_IMPLEMENT_SETTING.if_using_vector_rag

        if self.if_using_vector_rag and KAGGLE_IMPLEMENT_SETTING.rag_path:
            self.vector_base = KaggleExperienceBase(KAGGLE_IMPLEMENT_SETTING.rag_path)
            self.vector_base.path = Path(datetime.now(timezone.utc).strftime("%Y-%m-%d-%H-%M-%S") + "_kaggle_kb.pkl")
            self.vector_base.dump()

        self._output_format = self.output_format
        self._interface = self.interface
        self._simulator = self.simulator
        self._background = self.background

        self.action_counts = dict.fromkeys(KG_ACTION_LIST, 0)
        self.reward_estimates = {action: 0.0 for action in KG_ACTION_LIST}
        self.reward_estimates["Model feature selection"] = 0.2
        self.reward_estimates["Model tuning"] = 1.0
        self.confidence_parameter = 1.0
        self.initial_performance = 0.0

    def _analysis_competition_description(self):
        sys_prompt = (
            Environment(undefined=StrictUndefined)
            .from_string(prompt_dict["kg_description_template"]["system"])
            .render()
        )

        user_prompt = (
            Environment(undefined=StrictUndefined)
            .from_string(prompt_dict["kg_description_template"]["user"])
            .render(
                competition_descriptions=self.competition_descriptions,
                raw_data_information=self._source_data,
                evaluation_metric_direction=self.evaluation_metric_direction,
            )
        )

        response_analysis = APIBackend().build_messages_and_create_chat_completion(
            user_prompt=user_prompt,
            system_prompt=sys_prompt,
            json_mode=True,
        )

        response_json_analysis = json.loads(response_analysis)
        self.competition_type = response_json_analysis.get("Competition Type", "No type provided")
        self.competition_description = response_json_analysis.get("Competition Description", "No description provided")
        self.target_description = response_json_analysis.get("Target Description", "No target provided")
        self.competition_features = response_json_analysis.get("Competition Features", "No features provided")
        self.submission_specifications = response_json_analysis.get(
            "Submission Specifications", "No submission requirements provided"
        )
        self.model_output_channel = response_json_analysis.get("Submission channel number to each sample", 1)
        self.evaluation_desc = response_json_analysis.get(
            "Evaluation Description", "No evaluation specification provided."
        )

    def get_competition_full_desc(self) -> str:
        evaluation_direction = "higher the better" if self.evaluation_metric_direction else "lower the better"
        return f"""Competition Type: {self.competition_type}
    Competition Description: {self.competition_description}
    Target Description: {self.target_description}
    Competition Features: {self.competition_features}
    Submission Specifications: {self.submission_specifications}
    Model Output Channel: {self.model_output_channel}
    Evaluation Descriptions: {self.evaluation_desc}
    Is the evaluation metric the higher the better: {evaluation_direction}
    """

    @property
    def background(self) -> str:
        background_template = prompt_dict["kg_background"]

        train_script = (
            Path(__file__).parent / f"{KAGGLE_IMPLEMENT_SETTING.competition}_template" / "train.py"
        ).read_text()

        background_prompt = (
            Environment(undefined=StrictUndefined)
            .from_string(background_template)
            .render(
                train_script=train_script,
                competition_type=self.competition_type,
                competition_description=self.competition_description,
                target_description=self.target_description,
                competition_features=self.competition_features,
                submission_specifications=self.submission_specifications,
                evaluation_desc=self.evaluation_desc,
                evaluate_bool=self.evaluation_metric_direction,
            )
        )
        return background_prompt

    @property
    def source_data(self) -> str:
        data_folder = Path(KAGGLE_IMPLEMENT_SETTING.local_data_path) / self.competition

        if (data_folder / "X_valid.pkl").exists():
            X_valid = pd.read_pickle(data_folder / "X_valid.pkl")
            # TODO: Hardcoded for now, need to be fixed
            if self.competition == "feedback-prize-english-language-learning":
                self.input_shape = X_valid.shape
                return "This is a sparse matrix of descriptive text."
            buffer = io.StringIO()
            X_valid.info(verbose=True, buf=buffer, show_counts=True)
            data_info = buffer.getvalue()
            self.input_shape = X_valid.shape
            return data_info

        preprocess_experiment = KGFactorExperiment([])
        (
            X_train,
            X_valid,
            y_train,
            y_valid,
            X_test,
            *others,
        ) = preprocess_experiment.experiment_workspace.generate_preprocess_data()

        data_folder.mkdir(exist_ok=True, parents=True)
        pickle.dump(X_train, open(data_folder / "X_train.pkl", "wb"))
        pickle.dump(X_valid, open(data_folder / "X_valid.pkl", "wb"))
        pickle.dump(y_train, open(data_folder / "y_train.pkl", "wb"))
        pickle.dump(y_valid, open(data_folder / "y_valid.pkl", "wb"))
        pickle.dump(X_test, open(data_folder / "X_test.pkl", "wb"))
        pickle.dump(others, open(data_folder / "others.pkl", "wb"))

        self.input_shape = X_valid.shape

        buffer = io.StringIO()
        X_valid.info(verbose=True, buf=buffer, show_counts=True)
        data_info = buffer.getvalue()
        return data_info

    @property
    def output_format(self) -> str:
        return (
            Environment(undefined=StrictUndefined)
            .from_string(prompt_dict["kg_model_output_format"])
            .render(channel=self.model_output_channel)
        )

    @property
    def interface(self) -> str:
        return f"""The feature code should follow the interface:
{prompt_dict['kg_feature_interface']}
The model code should follow the interface:
{prompt_dict['kg_model_interface']}
"""

    @property
    def simulator(self) -> str:
        kg_model_simulator = (
            Environment(undefined=StrictUndefined)
            .from_string(prompt_dict["kg_model_simulator"])
            .render(submission_specifications=self.submission_specifications)
        )
        return f"""The feature code should follow the simulator:
{prompt_dict['kg_feature_simulator']}
The model code should follow the simulator:
{kg_model_simulator}
"""

    @property
    def rich_style_description(self) -> str:
        return f"""
This is the Kaggle scenario for the competition: {self.competition}
"""

    def get_scenario_all_desc(self, task: Task | None = None) -> str:
        return f"""Background of the scenario:
{self._background}
The source dataset you can use to generate the features:
{self._source_data}
The interface you should follow to write the runnable code:
{self._interface}
The output of your code should be in the format:
{self._output_format}
The simulator user can use to test your model:
{self._simulator}
The expected output & submission format specifications:
{self.submission_specifications} # Added again to emphasize the importance
"""
