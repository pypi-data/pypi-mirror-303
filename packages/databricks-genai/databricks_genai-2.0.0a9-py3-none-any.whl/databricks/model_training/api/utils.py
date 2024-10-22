"""Utility functions for the API."""

import hashlib
import logging
import os
from typing import Tuple

from databricks.sdk import WorkspaceClient
from IPython import get_ipython  # type: ignore

logger = logging.getLogger(__name__)

_LOCAL_DEV_CONFIG_PROFILE = 'DBX_DEV_LOCAL'
_DATABRICKS_CONFIG_PROFILE_ENV = 'DATABRICKS_CONFIG_PROFILE'
_TEST_CONFIG_PROFILE = 'DBX_DEV_TEST'


def is_running_in_databricks_notebook() -> bool:
    try:
        shell = get_ipython().__class__.__name__  # pylint: disable = undefined-variable
        if shell == 'DatabricksShell':
            return True
        return False
    except Exception:  # pylint: disable = broad-except
        return False


def get_me() -> str:
    """
    Get who is currently logged in.

    Returns:
        str: The name of the current user.
    """
    # TODO remove, only used for testing
    if os.environ.get(_DATABRICKS_CONFIG_PROFILE_ENV, '') in [
            _LOCAL_DEV_CONFIG_PROFILE,
            _TEST_CONFIG_PROFILE,
    ]:
        return 'me'

    w = WorkspaceClient()
    me = w.current_user.me().user_name or ''
    if not me:
        raise EnvironmentError('Could not determine the current user. Please check your environment.')
    logger.debug(f'You are {me}')
    return me


def _get_host_and_token_from_env() -> Tuple[str, str]:
    """
    Get the host and token from the environment

    In a databricks notebook, the host will be the underlying region and env (i.e. oregon.staging.databricks.com)
    """
    if os.environ.get(_DATABRICKS_CONFIG_PROFILE_ENV, '') == _TEST_CONFIG_PROFILE:
        return 'test', 'test'
    w = WorkspaceClient()
    if is_running_in_databricks_notebook():
        ctx = w.dbutils.entry_point.getDbutils().notebook().getContext()
        host = ctx.apiUrl().get()
        token = ctx.apiToken().get()
    else:
        host = w.config.host
        token = w.config.token
    if not host or not token:
        raise EnvironmentError('Could not find root URL and/or token. Please check your environment.')
    return host, token


def get_cluster_id() -> str:
    """
    Get the cluster ID from the environment
    """
    if os.environ.get(_DATABRICKS_CONFIG_PROFILE_ENV, '') == _TEST_CONFIG_PROFILE:
        return 'test'
    w = WorkspaceClient()
    if is_running_in_databricks_notebook():
        ctx = w.dbutils.notebook.entry_point.getDbutils().notebook().getContext()
        cluster_id = ctx.clusterId().get()
    else:
        cluster_id = w.config.cluster_id
    return cluster_id


def md5_hash(s: str, num_digits=8) -> str:
    return hashlib.md5(s.encode()).hexdigest()[:num_digits]
