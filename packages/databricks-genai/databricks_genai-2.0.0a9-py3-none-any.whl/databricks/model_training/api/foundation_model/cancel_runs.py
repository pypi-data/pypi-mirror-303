"""Cancel model training runs"""

import logging
from typing import Any, Dict, List, Union

from databricks.model_training.api.engine import get_return_response, run_plural_mapi_request
from databricks.model_training.api.exceptions import DatabricksModelTrainingRequestError
from databricks.model_training.types.training_run import TrainingRun

logger = logging.getLogger(__name__)

QUERY_FUNCTION = 'stopFinetunes'
VARIABLE_DATA_NAME = 'getFinetunesData'
OPTIONAL_DATA_NAME = 'stopFinetunesData'
QUERY = f"""
mutation StopFinetunes(${VARIABLE_DATA_NAME}: GetFinetunesInput!, ${OPTIONAL_DATA_NAME}: StopFinetunesInput) {{
  {QUERY_FUNCTION}({VARIABLE_DATA_NAME}: ${VARIABLE_DATA_NAME}, {OPTIONAL_DATA_NAME}: ${OPTIONAL_DATA_NAME}) {{
    id
    name
    status
    createdById
    createdByEmail
    createdAt
    updatedAt
    startedAt
    completedAt
    reason
    isDeleted
    details {{
            model
            trainDataPath
            saveFolder
            experimentTracker
        }}
  }}
}}"""


def cancel(experiment_ids: Union[str, List[str]]) -> int:
    """
    Cancel all sweep run(s) by experiment ID(s)

    Args:
        experiment_ids (str): List of experiment IDs to cancel

    Raises:
        DatabricksModelTrainingRequestError: Raised if stopping any of the requested runs failed

    Returns:
        int: The number of training runs canceled
    """
    if not experiment_ids:
        raise ValueError('Must provide valid experiment ID(s) to cancel.')
    if isinstance(experiment_ids, str):
        experiment_ids = [experiment_ids]
    filters = {'mlflowExperimentId': {'in': experiment_ids}}
    variables: Dict[str, Dict[str, Any]] = {
        VARIABLE_DATA_NAME: {
            'filters': filters
        },
        OPTIONAL_DATA_NAME: {
            'reason': 'Canceled by user.'
        }
    }

    try:
        response = run_plural_mapi_request(
            query=QUERY,
            query_function=QUERY_FUNCTION,
            return_model_type=TrainingRun,
            variables=variables,
        )
        canceled_runs = get_return_response(response)
        canceled_run_names = ', '.join([run.name for run in canceled_runs])
        num_canceled = len(canceled_runs)
        if num_canceled == 0:
            print('No active runs found to cancel.')
        else:
            print(f'Canceled {canceled_run_names} from {experiment_ids} successfully.')
        return num_canceled
    except Exception as e:
        raise DatabricksModelTrainingRequestError(
            f'Failed to cancel runs for experiment ID(s) {experiment_ids}. Please make sure the runs \
            have not completed or failed and try again.') from e


def cancel_run(run: Union[str, TrainingRun]) -> int:
    """
    Cancel a model training run.

    Args:
        run (Union[str, TrainingRun]): The training run to cancel

    Raises:
        DatabricksModelTrainingRequestError: Raised if stopping any of the requested runs failed

    Returns:
        int: The number of training runs canceled
    """
    if not run:
        raise ValueError('Must provide valid training run to cancel.')
    requested_run_name = run.name if isinstance(run, TrainingRun) else run
    return cancel_runs(runs=[requested_run_name])


def cancel_runs(runs: Union[List[str], List[TrainingRun]]) -> int:
    """
    Cancel a training run, list of training runs, or all runs under a single MLflow experiment ID without
    deleting them. If the run does not exist or if the run has already terminated, an error will be raised.

    Args:
        runs (Optional[Union[List[str], List[TrainingRun]]]): The
            training run(s) to cancel. Can be a single run or a list of runs.

    Raises:
        DatabricksModelTrainingRequestError: Raised if stopping any of the requested runs failed

    Returns:
        int: The number of training runs cancelled
    """
    if len(runs) < 1:
        raise ValueError('Must provide valid training run(s) to cancel.')
    filters = {}
    run_names_to_cancel = [getattr(run, 'name', run) for run in runs if run]
    filters['name'] = {'in': run_names_to_cancel}

    variables: Dict[str, Dict[str, Any]] = {
        VARIABLE_DATA_NAME: {
            'filters': filters
        },
        OPTIONAL_DATA_NAME: {
            'reason': 'Canceled by user.'
        }
    }

    try:
        response = run_plural_mapi_request(
            query=QUERY,
            query_function=QUERY_FUNCTION,
            return_model_type=TrainingRun,
            variables=variables,
        )
        canceled_runs = get_return_response(response)
        num_canceled = len(canceled_runs)
        if num_canceled == 0:
            print('No active runs found to cancel.')
        else:
            canceled_run_names = ', '.join([run.name for run in canceled_runs])
            not_found = ''
            if num_canceled < len(run_names_to_cancel):
                not_found = f' {len(run_names_to_cancel) - num_canceled} run(s) were not found or already terminated.'
            print(f'Canceled {canceled_run_names} successfully.{not_found}')
        return num_canceled
    except Exception as e:
        raise DatabricksModelTrainingRequestError(f'Failed to cancel runs {runs}. Please make sure the run \
                                                  has not completed or failed and try again.') from e
