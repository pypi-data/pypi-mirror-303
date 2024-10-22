""" Serving utilities """
from dataclasses import dataclass
from typing import Dict, Optional

from mlflow.tracking import MlflowClient

from databricks.model_training.types.train_config import TrainTaskType


@dataclass
class BaseModelDetails:
    system_ai_path: str
    version: str
    task_type: TrainTaskType


# Mapping from supported FT model name to the corresponding model path
# Models that are not supported by serving should be set to None.
# SUBSTITUTION: Some base models are not enabled for serving. Those models are substituted with their instruct versions.
FT_MODEL_PATH_MAPPING: Dict[str, Optional[str]] = {
    'codellama/CodeLlama-13b-Instruct-hf': None,
    'codellama/CodeLlama-13b-Python-hf': None,
    'codellama/CodeLlama-13b-hf': None,
    'codellama/CodeLlama-34b-Instruct-hf': None,
    'codellama/CodeLlama-34b-Python-hf': None,
    'codellama/CodeLlama-34b-hf': None,
    'codellama/CodeLlama-7b-Instruct-hf': None,
    'codellama/CodeLlama-7b-Python-hf': None,
    'codellama/CodeLlama-7b-hf': None,
    'databricks/dbrx-base': 'system.ai.dbrx_base',
    'databricks/dbrx-instruct': 'system.ai.dbrx_instruct',
    'meta-llama/Llama-2-13b-chat-hf': None,
    'meta-llama/Llama-2-13b-hf': None,
    'meta-llama/Llama-2-70b-chat-hf': None,
    'meta-llama/Llama-2-70b-hf': None,
    'meta-llama/Llama-2-7b-chat-hf': None,
    'meta-llama/Llama-2-7b-hf': None,
    'meta-llama/Llama-3.2-1B': 'system.ai.llama_v3_2_1b_instruct',  # SUBSTITUTION
    'meta-llama/Llama-3.2-1B-Instruct': 'system.ai.llama_v3_2_1b_instruct',
    'meta-llama/Llama-3.2-3B': 'system.ai.llama_v3_2_3b_instruct',  # SUBSTITUTION
    'meta-llama/Llama-3.2-3B-Instruct': 'system.ai.llama_v3_2_3b_instruct',
    'meta-llama/Meta-Llama-3-70B': 'system.ai.meta_llama_3_70b',
    'meta-llama/Meta-Llama-3-70B-Instruct': 'system.ai.meta_llama_3_70b_instruct',
    'meta-llama/Meta-Llama-3-8B': 'system.ai.meta_llama_3_8b',
    'meta-llama/Meta-Llama-3-8B-Instruct': 'system.ai.meta_llama_3_8b_instruct',
    'meta-llama/Meta-Llama-3.1-405B': 'system.ai.meta_llama_v3_1_405b',
    'meta-llama/Meta-Llama-3.1-405B-Instruct': 'system.ai.meta_llama_v3_1_405b_instruct_fp8',
    'meta-llama/Meta-Llama-3.1-70B': 'system.ai.meta_llama_v3_1_70b_instruct',  # SUBSTITUTION
    'meta-llama/Meta-Llama-3.1-70B-Instruct': 'system.ai.meta_llama_v3_1_70b_instruct',
    'meta-llama/Meta-Llama-3.1-8B': 'system.ai.meta_llama_v3_1_8b_instruct',  # SUBSTITUTION
    'meta-llama/Meta-Llama-3.1-8B-Instruct': 'system.ai.meta_llama_v3_1_8b_instruct',
    'mistralai/Mistral-7B-Instruct-v0.2': 'system.ai.mistral_7b_instruct_v0_2',
    'mistralai/Mistral-7B-v0.1': 'system.ai.mistral_7b_v0_1',
    'mistralai/Mixtral-8x7B-v0.1': 'system.ai.mixtral_8x7b_v0_1',
}


def get_base_model_details(model_name: str) -> BaseModelDetails:
    """
    Get the model path for the given model name

    Args:
        model_name (str): The FT base model name

    Returns:
        BaseModelDetails: model path, version, and task type
    """
    system_ai_path = FT_MODEL_PATH_MAPPING.get(model_name)
    if system_ai_path is None:
        raise ValueError(f"Model '{system_ai_path}' is not supported.")

    client = MlflowClient()
    model_versions = client.search_model_versions(f"name='{system_ai_path}'")
    latest_version = max(model_versions, key=lambda x: int(x.version))

    task_type = TrainTaskType.CHAT_COMPLETION if '_instruct' in system_ai_path else TrainTaskType.INSTRUCTION_FINETUNE

    return BaseModelDetails(system_ai_path=system_ai_path, version=latest_version.version, task_type=task_type)
