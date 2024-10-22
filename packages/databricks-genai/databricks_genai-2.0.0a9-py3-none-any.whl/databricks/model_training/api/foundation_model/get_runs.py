"""Get multiple model training runs"""

import logging
from datetime import datetime
from typing import List, Optional, Union

from databricks.model_training.api.engine import get_return_response, run_paginated_mapi_request
from databricks.model_training.api.validation import parse_datetime
from databricks.model_training.types import TrainingRun
from databricks.model_training.types.common import ObjectList
from databricks.model_training.types.run_status import RunStatus

logger = logging.getLogger(__name__)

DEFAULT_RUN_LIMIT = 20

QUERY_FUNCTION = 'getFinetunesPaginated'
VARIABLE_DATA_NAME = 'getFinetunesPaginatedData'
QUERY = f"""
query GetFinetunesPaginated(${VARIABLE_DATA_NAME}: GetFinetunesPaginatedInput!) {{
  {QUERY_FUNCTION}({VARIABLE_DATA_NAME}: ${VARIABLE_DATA_NAME}) {{
    cursor
    hasNextPage
    finetunes {{
        id
        name
        status
        createdByEmail
        createdAt
        updatedAt
        startedAt
        completedAt
        reason
        estimatedEndTime
        isDeleted
        details {{
            model
            taskType
            trainDataPath
            saveFolder
            evalDataPath
            trainingDuration
            learningRate
            contextLength
            experimentTracker
            customWeightsPath
            dataPrepConfig
            formattedFinetuningEvents {{
                eventType
                eventTime
                eventMessage
            }}
        }}
    }}
  }}
}}"""


def get_run(training_run: Optional[Union[str, TrainingRun]] = None,) -> TrainingRun:
    """Get a single training run

    Args:
        training_run: The training run to get
    Returns:
        A single TrainingRun object
    """
    training_run_name = ''
    if training_run is not None:
        training_run_name = training_run.name if isinstance(training_run, TrainingRun) else training_run
    runs = get_runs(training_runs=[training_run_name], limit=1)

    if not runs:
        raise ValueError(f'Run {training_run} not found.')
    return runs[0]


def get_runs(
    training_runs: Optional[Union[List[str], List[TrainingRun], ObjectList[TrainingRun]]] = None,
    *,
    statuses: Optional[Union[List[str], List[RunStatus]]] = None,
    user_emails: Optional[List[str]] = None,
    before: Optional[Union[str, datetime]] = None,
    after: Optional[Union[str, datetime]] = None,
    limit: Optional[int] = DEFAULT_RUN_LIMIT,
) -> ObjectList[TrainingRun]:
    """List training runs

    Args:
        training_runs (Optional[Union[List[str], List[TrainingRun], ObjectList[TrainingRun]]], optional):
        Training runs to fetch data for. This is a list of run names or TrainingRun objects. Defaults to None.
        statuses (Optional[Union[List[str], List[RunStatus]], optional): The statuses to filter by. Defaults to None.
        user_emails (Optional[List[str]], optional): The user emails to filter by. Defaults to None.
        before (Optional[Union[str, datetime]], optional): The date to filter before. Defaults to None.
        after (Optional[Union[str, datetime]], optional): The date to filter after. Defaults to None.
        limit (Optional[int], optional): The maximum number of runs to return. Defaults to the 20 most recent.

    Returns:
        ObjectList[TrainingRun]: A list of training runs
    """
    filters = {}
    if training_runs:
        filters['name'] = {'in': [getattr(r, 'name', r) for r in training_runs]}
    if statuses:
        filters['status'] = {'in': [s.value if isinstance(s, RunStatus) else s for s in statuses]}
    if before or after:
        date_filters = {}
        if before:
            date_filters['lt'] = before.astimezone().isoformat() if isinstance(before,
                                                                               datetime) else parse_datetime(before)
        if after:
            date_filters['gte'] = after.astimezone().isoformat() if isinstance(after,
                                                                               datetime) else parse_datetime(after)
        filters['createdAt'] = date_filters

    variables = {
        VARIABLE_DATA_NAME: {
            'filters': filters,
            'includeDeleted': False,
            'limit': limit,
        },
    }

    if user_emails:
        if variables[VARIABLE_DATA_NAME].get('entity'):
            variables[VARIABLE_DATA_NAME]['entity']['emails'] = user_emails
        else:
            variables[VARIABLE_DATA_NAME]['entity'] = {'emails': user_emails}

    response = run_paginated_mapi_request(
        query=QUERY,
        query_function=QUERY_FUNCTION,
        return_model_type=TrainingRun,
        variables=variables,
    )
    print(f'Returning the last {limit} runs.')
    return get_return_response(response)
