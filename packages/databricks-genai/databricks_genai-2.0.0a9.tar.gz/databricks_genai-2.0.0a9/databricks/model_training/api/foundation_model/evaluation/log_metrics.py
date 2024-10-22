"""Log eval metrics as FT RunEvent"""

from typing import List

from databricks.model_training.api.engine import get_return_response, run_singular_mapi_request
from databricks.model_training.types import EvalMetricDict, RunEvent

QUERY_FUNCTION = 'createRunEvent'
VARIABLE_DATA_NAME = 'createRunEventData'

QUERY = f"""
mutation CreateRunEvent(${VARIABLE_DATA_NAME}: CreateRunEventInput!) {{
    {QUERY_FUNCTION}({VARIABLE_DATA_NAME}: ${VARIABLE_DATA_NAME}) {{
        eventData
        eventType
        executionId
        id
        runId
        updatedAt
    }}
}}"""


def log_metrics(
    run_name: str,
    dataset_id: str,
    eval_metrics: List[EvalMetricDict],
) -> None:
    """
    Logs evaluation metrics as RunEvent

    Args:
        run_name (str): The name of the run to log the metrics for.
        dataset_id (str): Some identifier for the dataset. This can be a name, filepath, etc.
        eval_metrics (List[EvalMetric]): A list of evaluation metrics to log.
    """
    if len(eval_metrics) == 0:
        raise ValueError('No evaluation metrics provided.')
    for metric in eval_metrics:
        if not all(key in metric for key in ['metric_name', 'score', 'greater_is_better']):
            raise ValueError(
                "Each evaluation metric must contain 'metric_name', 'score', and 'greater_is_better' fields.")

    metrics = [{
        'metricName': metric['metric_name'],
        'score': metric['score'],
        'greaterIsBetter': metric['greater_is_better'],
        'baselineScore': metric.get('baseline_score'),
    } for metric in eval_metrics]
    variables = {
        VARIABLE_DATA_NAME: {
            'eventData': {
                'evalDatasetId': dataset_id,
                'metrics': metrics,
            },
            'eventType': 'LOG_EVALUATION_METRIC',
            'runName': run_name,
        }
    }

    response = run_singular_mapi_request(
        query=QUERY,
        query_function=QUERY_FUNCTION,
        return_model_type=RunEvent,
        variables=variables,
    )

    try:
        get_return_response(response)
    except Exception as e:
        raise ValueError(f'Failed to log evaluation results. {e}') from e

    print(f'Logged evaluation results for run {run_name}.')
