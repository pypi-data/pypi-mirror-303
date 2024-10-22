"""
Input to create a sweep.
"""
import logging
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from mcli.utils.utils_config import strip_nones
from mcli.utils.utils_string_functions import snake_case_to_camel_case

from databricks.model_training.api.exceptions import DatabricksGenAIConfigError

logger = logging.getLogger(__name__)


@dataclass
class SweepInput:
    """
    Input to create a Sweep and its training runs.

    Args:
        task_type (str): Task type to finetune on.
        models (List[str]): A list of models. We currently can only take one model.
        train_data_paths (List[str]): A list of training data paths. We currently can only take one train data path.
        model_registry_path (str): The path to the model registry.
        save_folder (str): The folder to save checkpoints.
        eval_data_path (Optional[str], optional): The path to the evaluation data. Defaults to None.
        training_durations (Optional[List[int]], optional): A list of training durations. Defaults to None.
            We generate learning rates and training durations if both aren't provided and submitted model
            supports auto sweep.
        learning_rates (Optional[List[float]], optional): A list of learning rates. Defaults to None.
            We generate learning rates and training durations if both aren't provided and submitted model
            supports auto sweep.
        context_length (Optional[int], optional): The length of the context. Defaults to None.
        experiment_name (Optional[str], optional): The name of the MLflow experiment to create. Defaults to None.
        experiment_directory (Optional[str], optional): The directory of the MLflow experiment to create.
            Defaults to None.
        custom_weights_path (Optional[str], optional): The path to custom weights. Defaults to None.
        data_prep_config (Optional[Dict], optional): The data preparation configuration. Defaults to None.

    Returns:
        None
    """

    task_type: str
    models: List[str]
    train_data_paths: List[str]
    model_registry_path: str
    save_folder: str
    eval_data_path: Optional[str] = None
    training_durations: Optional[List[int]] = None
    learning_rates: Optional[List[float]] = None
    context_length: Optional[int] = None
    experiment_name: Optional[str] = None
    experiment_directory: Optional[str] = None
    custom_weights_path: Optional[str] = None
    data_prep_config: Optional[Dict] = None

    _required_properties = {'models', 'train_data_paths', 'model_registry_path', 'save_folder'}
    _sweep_properties = {
        'task_type',
        'models',
        'train_data_paths',
        'model_registry_path',
        'save_folder',
        'eval_data_path',
        'training_durations',
        'learning_rates',
        'context_length',
        'experiment_name',
        'experiment_directory',
        'custom_weights_path',
        'data_prep_config',
    }

    @classmethod
    def validate_dict(cls, dict_to_use: Dict, show_unused_warning: bool = True) -> Dict:
        """Validate the sweep input from the provided dictionary.
        """
        sweep_input_dict = strip_nones(dict_to_use)
        unused_keys = set(sweep_input_dict) - cls._sweep_properties
        for key in unused_keys:
            del sweep_input_dict[key]
        missing = cls._required_properties - set(dict_to_use)
        if missing:
            raise DatabricksGenAIConfigError(f'Missing required fields: {", ".join(missing)}',)
        if len(unused_keys) > 0 and show_unused_warning:
            raise DatabricksGenAIConfigError(f'Encountered unknown fields in sweep input: {", ".join(unused_keys)}.')
        return sweep_input_dict

    @classmethod
    def from_dict(cls, dict_to_use: Dict[str, Any], show_unused_warning: bool = True):
        """Load the sweep input from the provided dictionary.
        """
        sweep_input_dict = cls.validate_dict(dict_to_use, show_unused_warning)
        return cls(**sweep_input_dict)

    def to_create_api_input(self) -> Dict[str, Dict[str, Any]]:
        """Converts the TrainConfig object to Compute and Finetune that can be used to create a finetune run
        """
        sweep_input = {}
        sweep_input_dict = strip_nones(self.__dict__)
        for key, val in sweep_input_dict.items():
            translated_key = snake_case_to_camel_case(key)
            sweep_input[translated_key] = val

        return {'sweepInput': sweep_input}
