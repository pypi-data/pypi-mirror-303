"""
Get model training sweep
"""
from datetime import datetime
from typing import List, Optional, Union

from databricks.model_training.api.engine import get_return_response, run_plural_mapi_request
from databricks.model_training.api.validation import parse_datetime
from databricks.model_training.types.common import ObjectList
from databricks.model_training.types.sweep import Sweep
from databricks.model_training.types.sweep_status import SweepStatus

DEFAULT_SWEEP_LIMIT = 5

QUERY_FUNCTION = 'getFinetuneSweeps'
VARIABLE_DATA_NAME = 'getFinetuneSweepsData'

QUERY = f"""
query GetFinetuneSweeps(${VARIABLE_DATA_NAME}: GetFinetuneSweepsInput!) {{
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
        updatedAt
        startedAt
        completedAt
        reason
        estimatedEndTime
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


def get(
    experiment_ids: Optional[Union[str, List[str]]] = None,
    *,
    statuses: Optional[Union[List[str], List[SweepStatus]]] = None,
    before: Optional[Union[str, datetime]] = None,
    after: Optional[Union[str, datetime]] = None,
    limit: Optional[int] = DEFAULT_SWEEP_LIMIT,
) -> ObjectList[Sweep]:
    """
    Get sweep details filtered by MLflow experiment IDs, statuses, and creation date.

    Args:
        experiment_ids (Optional[Union[str,List[str]]]): List of MLflow experiment IDs or a single experiment
            ID to filter the sweeps by.
        statuses (Optional[Union[List[str], List[RunStatus]]]): Filter by the status of the sweeps.
        before (Optional[Union[str, datetime]]): Filter sweeps created before a specific date in user's local time.
        after (Optional[Union[str, datetime]]): Filter sweeps created after a specific date in user's local time.

    Returns:
        ObjectList[Sweep]: The sweep details associated with the given filters.
    """
    filters = {}
    if experiment_ids:
        if isinstance(experiment_ids, str):
            experiment_ids = [experiment_ids]
        filters = {'mlflowExperimentId': {'in': experiment_ids}}
    if statuses:
        filters['sweepStatus'] = {'in': [s.value if isinstance(s, SweepStatus) else s for s in statuses]}
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
            'limit': limit
        },
    }

    response = run_plural_mapi_request(
        query=QUERY,
        query_function=QUERY_FUNCTION,
        return_model_type=Sweep,
        variables=variables,
    )

    return get_return_response(response)
