"""Provisioned throughput endpoint for model serving"""

import json
import re
import time

import requests
from mlflow.deployments import DatabricksEndpoint, get_deploy_client
from requests.exceptions import HTTPError

from databricks.model_training.api.utils import _get_host_and_token_from_env, get_me, md5_hash
from databricks.model_training.types.train_config import TrainTaskType


class ProvisionedThroughputEndpoint:
    """
    Represents a provisioned throughput endpoint of a fine-tuned model that can generate text from a
    model. The endpoint is accessed through the Databricks Model Serving REST
    API and MLFlow Deployments library.

    Args:
        uc_model_path (str): The UC location of the model to be served. Ex: 'system.ai.dbrx_instruct'
        model_version (str): The version of the model to be served. Ex: '3'
        task_type (str): The task type of the model. Default is 'CHAT_COMPLETION'.
        scale_to_zero_enabled (bool): If True, the endpoint will scale to zero when not in use. Default is True.
        chunk_size_multiplier (int): The multiplier for the serving throughput chunk size. Default is 1.
        block_until_ready (bool): If True, the endpoint will block on returning until it is ready. Default is True.
    """

    def __init__(
        self,
        uc_model_path: str,
        model_version: str,
        task_type: str = 'CHAT_COMPLETION',
        scale_to_zero_enabled: bool = True,
        chunk_size_multiplier: int = 1,
        block_until_ready: bool = True,
    ) -> None:
        self._validate_inputs(uc_model_path, task_type, chunk_size_multiplier)

        model_name = uc_model_path.split('.')[-1]
        self.endpoint_name = self._generate_endpoint_name(model_name, model_version)
        self.deployment_endpoint = f'endpoints:/{self.endpoint_name}'

        self.task_type = TrainTaskType(task_type)

        # PT Config
        throughput_chunk_size = self._get_throughput_chunk_size(uc_model_path, model_version)
        self.config = {
            'served_entities': [{
                'name': self.endpoint_name,
                'entity_name': uc_model_path,
                'entity_version': model_version,
                'workload_size': 'Small',
                'workload_type': 'GPU_SMALL',
                'scale_to_zero_enabled': scale_to_zero_enabled,
                'min_provisioned_throughput': 0,
                'max_provisioned_throughput': chunk_size_multiplier * throughput_chunk_size,
            }],
        }

        self.block_until_ready = block_until_ready

        dbx_client = get_deploy_client('databricks')
        if dbx_client is None:
            raise RuntimeError('Failed to get Databricks deploy client.')
        self.client = dbx_client

        self.endpoint = self.start_pt_endpoint()

        if self.block_until_ready:
            print(f'Provisioned throughput endpoint is starting at {self.endpoint_name}. Waiting for it to be ready...')
            self.wait_for_pt_endpoint_ready()
            print(f'Provisioned throughput endpoint is ready at {self.deployment_endpoint}')
        else:
            print(f'Provisioned throughput endpoint is starting at {self.deployment_endpoint}. '
                  f"Please wait for endpoint to be ready with '{self.__class__.wait_for_pt_endpoint_ready.__name__}' "
                  'before use.')

    def __enter__(self) -> 'ProvisionedThroughputEndpoint':
        return self

    def __exit__(self, _exc_type, _exc_value, _traceback) -> None:
        self.teardown_pt_endpoint()

    def __str__(self):
        return self.deployment_endpoint

    @staticmethod
    def _validate_inputs(uc_model_path: str, task_type: str, chunk_size_multiplier: int) -> None:
        """
        Validates input arguments for initialization.
        """
        model_path_regex = r'^[^/. ]+\.[^/. ]+\.[^/. ]+$'
        if not re.match(model_path_regex, uc_model_path):
            raise ValueError(
                f'Invalid uc_model_path {uc_model_path}. ' \
                "Please specify a UC location in the format '<catalog>.<schema>.<model>'. " \
                "This should be indicated under the 'Details' section on the model's page in your workspace.")

        serving_task_types = {TrainTaskType.INSTRUCTION_FINETUNE.value, TrainTaskType.CHAT_COMPLETION.value}
        if task_type not in serving_task_types:
            raise ValueError('Please specify a valid task type for the model. '
                             f'Supported task types are {serving_task_types}.')

        if chunk_size_multiplier <= 0:
            raise ValueError('Please specify a chunk size multiplier greater than 0.')

    @staticmethod
    def _generate_endpoint_name(model_name: str, model_version: str) -> str:
        """
        Helper function that generates a unique endpoint name for the PT
        endpoint. Name is unique per-user and model to avoid conflicts.
        """
        user = get_me()
        hashed_user = md5_hash(user, num_digits=8)
        # rules: must be alphanumeric w/ hyphens and less than 64 characters
        endpoint_name = '-'.join([model_name[:44], f'v{model_version[:3]}', 'eval', hashed_user])
        endpoint_name = ''.join([c if c.isalnum() or c == '-' else '-' for c in endpoint_name])
        return endpoint_name

    @staticmethod
    def _get_throughput_chunk_size(uc_model_path: str, model_version: str) -> int:
        """
        Makes an request to the `serving_endpoints` API endpoint to get the
        optimized throughput chunk size. This is required for PT serving of
        fine-tuned models.
        """
        host, token = _get_host_and_token_from_env()

        base_url = f'{host}/api/2.0/serving-endpoints'
        optimization_info_url = base_url + f'/get-model-optimization-info/{uc_model_path}/{model_version}'
        request_headers = {
            'Context-Type': 'text/json',
            'Authorization': f'Bearer {token}',
        }
        response = requests.get(url=optimization_info_url, headers=request_headers, timeout=10)
        if response.status_code != 200:
            raise HTTPError(f'Failed to retrieve throughput chunk size. Error {response.status_code}: {response.text}')

        throughput_information = response.json()
        throughput_chunk_size = throughput_information.get('throughput_chunk_size')

        # If `optimizable` is False, then we can't get `throughput_chunk_size`
        # because the model isn't supported by Databricks Model Serving.
        if throughput_chunk_size is None:
            optimizable = throughput_information.get('optimizable', False)
            if not optimizable:
                raise ValueError('Please use a model that is currently supported by Databricks Model serving: '
                                 'https://docs.databricks.com/en/machine-learning/foundation-models/index.html'
                                 '#provisioned-throughput-foundation-model-apis')
            raise ValueError('Could not retrieve throughput chunk size from '
                             '`serving-endpoints/model-optimization-info`. '
                             f'{json.dumps(throughput_information)}')

        return throughput_chunk_size

    def is_endpoint_ready(self) -> bool:
        """
        Returns True if the endpoint is scaled from zero and ready to serve
        requests. Returns False otherwise.
        """
        return self.endpoint.state.ready == 'READY'

    def start_pt_endpoint(self) -> DatabricksEndpoint:
        """
        Spins up a provisioned throughput endpoint on behalf of the user's
        provided model.
        """
        try:
            existing_endpoint = self.client.get_endpoint(self.endpoint_name)
            print(f'Endpoint {self.endpoint_name} already exists. Skipping endpoint creation. '
                  f"Please wait for endpoint to be ready with '{self.__class__.wait_for_pt_endpoint_ready.__name__}' "
                  'before use.')
            return existing_endpoint
        except HTTPError as e:
            if e.response.status_code != 404:
                raise e

        # Create the endpoint through a POST request
        endpoint = self.client.create_endpoint(name=self.endpoint_name, config=self.config)

        return endpoint

    def wait_for_pt_endpoint_ready(self, timeout_mins: int = 30, check_interval_secs: int = 30):
        """
        Waits for the PT endpoint to be ready before returning to the user.
        """
        t0 = time.time()
        timeout_secs = timeout_mins * 60
        while time.time() - t0 < timeout_secs:
            # refresh endpoint state
            try:
                self.endpoint = self.client.get_endpoint(self.endpoint_name)
            except HTTPError as e:
                if e.response.status_code == 404:
                    print(f'Endpoint {self.endpoint_name} does not exist. Please validate your served model endpoint '
                          'and spin it up manually if necessary.')
                    return
            state = self.endpoint.state
            if state['ready'] == 'READY':
                return
            if state['config_update'] == 'UPDATE_FAILED':
                raise RuntimeError('Endpoint update failed. Please validate your served model endpoint and spin'
                                   ' it down manually if necessary.')
            if state['config_update'] == 'UPDATE_CANCELED':
                raise RuntimeError('Endpoint update was canceled. Please validate your served model endpoint and spin'
                                   ' it down manually if necessary.')
            time.sleep(check_interval_secs)

        raise TimeoutError(f'Provisioned throughput endpoint was not ready within {timeout_mins} minutes.')

    def teardown_pt_endpoint(self):
        """
        Tears down the provisioned throughput endpoint.
        """
        if self.is_endpoint_ready():
            self.client.delete_endpoint(self.endpoint_name)
            print(f'Endpoint {self.endpoint_name} has been torn down.')
        else:
            print(f'Endpoint {self.endpoint_name} is not ready. Skipping teardown.')

    def query(self, input_data: dict) -> str:
        """
        Queries the PT endpoint with the given input.

        Args:
            input_data (dict): Input data (or arguments) to pass to the deployment or model endpoint for inference.
        """
        if not self.is_endpoint_ready():
            raise RuntimeError('Provisioned throughput endpoint is not ready.'
                               'Please start it with `start_pt_endpoint`.')

        chat_response = self.client.predict(
            endpoint=self.endpoint_name,
            inputs=input_data,
        )
        if not chat_response:
            raise RuntimeError(f'Failed to generate completion for input: {input_data}')

        if self.task_type == TrainTaskType.INSTRUCTION_FINETUNE:
            msg = chat_response['choices'][0]['text']
        elif self.task_type == TrainTaskType.CHAT_COMPLETION:
            msg = chat_response['choices'][0]['message']['content']
        else:
            raise ValueError(f'Unsupported task type configured: {self.task_type.value}')

        return msg

    def generate_completion(self, prompt: str, temperature: float = 1.0, max_tokens: int = 128) -> str:
        """
        Uses PT endpoint to generate completion for a given prompt string.

        Args:
            prompt (str): The prompt to generate completion for.
            temperature (float): The temperature to use for sampling. Default is 1.0.
            max_tokens (int): The maximum number of tokens to generate. Default is 128.
        """
        if self.task_type == TrainTaskType.INSTRUCTION_FINETUNE:  # completions endpoint
            inputs = {
                'prompt': prompt,
                'temperature': temperature,
                'max_tokens': max_tokens,
            }
        elif self.task_type == TrainTaskType.CHAT_COMPLETION:  # chat endpoint
            inputs = {
                'messages': [{
                    # TODO: add a system prompt here?
                    'role': 'user',
                    'content': prompt,
                }],
                'temperature': temperature,
                'max_tokens': max_tokens,
            }
        else:
            raise ValueError(f'Unsupported task type configured: {self.task_type.value}')

        return self.query(inputs)
