"""Create a Sweep of finetuning runs"""

import logging
from typing import Dict, List, Optional, Union

from databricks.model_training.api.engine import get_return_response, run_singular_mapi_request
from databricks.model_training.api.utils import get_me
from databricks.model_training.api.validation import (SAVE_FOLDER_PATH, format_path, get_experiment_dir_and_name,
                                                      is_cluster_sql, validate_create_sweep_inputs)
from databricks.model_training.types import Sweep
from databricks.model_training.types.sweep_input import SweepInput
from databricks.model_training.types.train_config import TrainTaskType

logger = logging.getLogger(__name__)

QUERY_FUNCTION = 'createFinetuneSweep'
VARIABLE_DATA_NAME = 'createFinetuneSweepData'

QUERY = f"""
mutation CreateFinetuneSweep(${VARIABLE_DATA_NAME}: CreateFinetuneSweepInput!) {{
  {QUERY_FUNCTION}({VARIABLE_DATA_NAME}: ${VARIABLE_DATA_NAME}) {{
    mlflowExperimentId
    createdAt
    sweepStatus
    reason
    finetunes {{
        id
        name
        status
        createdByEmail
        createdAt
        startedAt
        updatedAt
        completedAt
        estimatedEndTime
        reason
        details {{
            model
            taskType
            trainDataPath
            saveFolder
            evalDataPath
            trainingDuration
            learningRate
            contextLength
            dataPrepConfig
            experimentTracker
            customWeightsPath
        }}
    }}
  }}
}}"""


def create(
    model: str,
    train_data_path: str,
    register_to: str,
    *,
    experiment_path: Optional[str] = None,
    task_type: Optional[str] = 'INSTRUCTION_FINETUNE',
    eval_data_path: Optional[str] = None,
    custom_weights_path: Optional[str] = None,
    training_durations: Optional[Union[List[str], str]] = None,
    learning_rates: Optional[Union[List[float], float]] = None,
    context_length: Optional[int] = None,
    data_prep_cluster_id: Optional[str] = None,
    validate_inputs: Optional[bool] = True,
) -> Sweep:
    """Create a foundation model hyperparameter sweep.

    Args:
        model (str): The Hugging Face name of the base model to fine-tune.
        train_data_path (str): The full remote location of your training data.
            The format of this data depends on the task type:
            - ``INSTRUCTION_FINETUNE``: JSONL format, where each line is a
              prompt and response JSON object. Example:
              {"prompt": "What is the capital of France?", "response": "Paris"}
            - ``CHAT_COMPLETION``: JSONL format, where each line is a list of messages.
              Example:
              [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello, I need some help with my task."},
                {"role": "assistant", "content": "Yes, I can help you with that. What do you need?"}
              ]
            - ``CONTINUED_PRETRAIN``: not currently supported for Sweeps.
        register_to (str): A Unity Catalog location where the model will be registered
            after training for easy deployment. Specify a location as either
            ``<catalog_name>.<schema_name>`` or ``<catalog_name>.<schema_name>.<model_name>``.
            The former will create a model with the same name as the training run.
        experiment_path (Optional[str], optional): The path to the directory to create the MLflow experiment.
            Defaults to ``Users/<your username>/<generated sweep name>``.
        task_type (Optional[str], optional): The type of task to train for. Options:
            - ``INSTRUCTION_FINETUNE``: (default): Fine-tune a model with instructions for a specific task.
            - ``CHAT_COMPLETION``: Finetune a model with chat message data.
            - ``CONTINUED_PRETRAIN``: not currently supported.
        eval_data_path (Optional[str], optional): The remote location of your evaluation data, if any.
            It must follow the same format as ``train_data_path``. Defaults to ``None``.
        custom_weights_path (Optional[str], optional): The remote location of a custom model
            checkpoint to use for the training run. If provided, these weights will be
            used instead of the model's pretrained weights. Must be an MLflow artifact path to your Composer checkpoint
            of your previously trained finetuned model on Databricks. Defaults to ``None``.
        training_durations (Optional[Union[List[str], str]], optional): A list of the total durations to launch for your
        training runs. Can be specified in:
            - Epochs (e.g. ``10ep``)
            - Tokens (e.g. ``1_000_000tok``)
            If not provided, research-backed parameters will be auto-generated based on the model you want to train.
        learning_rates (Optional[Union[List[float], float]], optional): A list of the peak learning rates to
            use for the training runs. If not provided, research-backed parameters will be auto-generated based on the
            model you want to train.
        context_length (Optional[int], optional): The maximum sequence length to use, truncating
            any data that exceeds it. Defaults to the Hugging Face model's default context
            length. Extending beyond the model's default context length is not supported.
        data_prep_cluster_id (Optional[str], optional): The cluster ID for Spark data processing.
            Required when using Delta tables as input because the underlying Delta files
            must be concatenated into a single location and converted to JSONL for
            instruction fine-tuning (IFT).
    Returns:
        Sweep: The sweep object that was created.
    """
    if experiment_path is None:
        experiment_directory = f'/Users/{get_me()}/'
        experiment_name = None
    else:
        experiment_directory, experiment_name = get_experiment_dir_and_name(experiment_path)

    train_data_path = format_path(train_data_path)
    if eval_data_path is not None:
        eval_data_path = format_path(eval_data_path)
    if custom_weights_path is not None:
        custom_weights_path = format_path(custom_weights_path)
    save_folder = SAVE_FOLDER_PATH
    if validate_inputs:
        validate_create_sweep_inputs(train_data_path, register_to, eval_data_path, data_prep_cluster_id,
                                     custom_weights_path, TrainTaskType(task_type))

    data_prep_config: Optional[Dict[str, Union[str, bool]]] = None
    # TODO: add translations for snake to camel case
    if data_prep_cluster_id is not None:
        data_prep_config = {'clusterId': data_prep_cluster_id}
        if is_cluster_sql(data_prep_cluster_id):
            data_prep_config['useSql'] = True

    learning_rates_list: List[float] = []
    training_durations_list: List[str] = []

    if isinstance(learning_rates, float):
        learning_rates_list = [learning_rates]
    elif isinstance(learning_rates, list):
        if not all(isinstance(lr, float) for lr in learning_rates):
            raise TypeError('Found non-float in list provided for learning_rates.')
        learning_rates_list = learning_rates

    if isinstance(training_durations, str):
        training_durations_list = [training_durations]
    elif isinstance(training_durations, list):
        if not all(isinstance(td, str) for td in training_durations):
            raise TypeError('Found non-string in list provided for training_durations.')
        training_durations_list = training_durations

    sweep_input = SweepInput.from_dict({
        'models': [model],
        'task_type': task_type,
        'train_data_paths': [train_data_path],
        'model_registry_path': register_to,
        'save_folder': save_folder,
        'eval_data_path': eval_data_path,
        'training_durations': training_durations_list,
        'learning_rates': learning_rates_list,
        'context_length': context_length,
        'experiment_directory': experiment_directory,
        'experiment_name': experiment_name,
        'custom_weights_path': custom_weights_path,
        'data_prep_config': data_prep_config,
    })
    sweep_input = sweep_input.to_create_api_input()
    variables = {
        VARIABLE_DATA_NAME: sweep_input,
    }
    response = run_singular_mapi_request(
        query=QUERY,
        query_function=QUERY_FUNCTION,
        return_model_type=Sweep,
        variables=variables,
    )
    sweep = get_return_response(response)
    print(f'Created {len(sweep.finetunes)} runs.')
    return sweep
