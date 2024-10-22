"""
Utilities for formatting foundation model training objects.
"""
from typing import Any, Dict, List
from urllib.parse import urljoin

from databricks.model_training.api.utils import _get_host_and_token_from_env, is_running_in_databricks_notebook


def get_mlflow_experiment_link_html(experiment_id: str, link_text: str = 'experiment') -> str:
    """
    Helper function to get a link for the MLflow experiment using the given experiment ID.
    """
    if is_running_in_databricks_notebook():
        host = ''
    else:
        host, _ = _get_host_and_token_from_env()
    path = urljoin(host, f'/ml/experiments/{experiment_id}')
    return f"<a href={path} class target='_blank'>{link_text}</a>"


def get_mlflow_run_link_html(experiment_id: str, run_id: str, link_text: str = 'run') -> str:
    """
    Helper function to get a link for the MLflow run using the given experiment ID and run ID.
    """
    if is_running_in_databricks_notebook():
        host = ''
    else:
        host, _ = _get_host_and_token_from_env()
    path = urljoin(host, f'/ml/experiments/{experiment_id}/runs/{run_id}')
    return f"<a href={path} class target='_blank'>{link_text}</a>"


def create_horizontal_html_table(data: List[Dict[str, Any]], key_to_label: Dict[str, str]) -> str:
    """
    Helper function to generate a horizontal HTML table.

    Parameters
    ----------
    data : List[Dict[str, Any]]
        A list of dictionaries where each dictionary represents a row.
    key_to_label : Dict[str, str]
        A dictionary mapping the keys in the data to the desired column headers.

    Returns
    -------
    str
        An HTML table as a string with headers in the first row and data in the subsequent rows.
    """
    res = []
    res.append("<table border=\"1\" class=\"dataframe\">")

    # Header row (labels from key_to_label)
    res.append('<thead>')
    res.append('<tr>')
    for key in key_to_label:
        res.append(f'<th style="text-align: left;">{key_to_label[key]}</th>')
    res.append('</tr>')
    res.append('</thead>')

    # Body rows (data)
    res.append('<tbody>')
    for row in data:
        res.append('<tr>')
        for key in key_to_label:
            value = row.get(key, None)
            res.append(f'<td style="text-align: left;">{value if value is not None else "-"}</td>')
        res.append('</tr>')
    res.append('</tbody>')

    res.append('</table>')
    return '\n'.join(res)


def create_vertical_html_table(data: List[Dict[str, Any]], key_to_label: Dict[str, str]) -> str:
    """
    Helper function to generate a vertical HTML table.

    Parameters
    ----------
    data : List[Dict[str, Any]]
        A list of dictionaries where each dictionary represents a row.
    key_to_label : Dict[str, str]
        A dictionary mapping the keys in the data to the desired row headers.

    Returns
    -------
    str
        An HTML table as a string with headers in the first column and values in the remaining columns.
    """
    res = []
    res.append("<table border='1' class='dataframe'>")
    res.append('<tbody>')

    # Each key becomes a row, with its values spread out across columns
    for key, label in key_to_label.items():
        res.append('<tr>')
        res.append(f'<th style="text-align: left;">{label}</th>')
        for row in data:
            value = row.get(key, None)
            res.append(f'<td style="text-align: left;">{value if value is not None else "-"}</td>')
        res.append('</tr>')

    res.append('</tbody>\n</table>')
    return '\n'.join(res)
