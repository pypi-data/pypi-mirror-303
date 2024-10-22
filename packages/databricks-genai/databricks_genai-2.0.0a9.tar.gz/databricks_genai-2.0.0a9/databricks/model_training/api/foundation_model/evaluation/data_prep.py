"""
Specifies functions that prepare data for evaluation.
Preparation supports any format that works with Mosaic AI Training.
See https://docs.databricks.com/en/large-language-models/foundation-model-training/data-preparation.html
"""
import os
from typing import Optional, Tuple
from uuid import uuid4

import datasets as hf_datasets
import pandas as pd
from databricks.connect import DatabricksSession
from pyspark.sql import DataFrame

from databricks.model_training.api.utils import _get_host_and_token_from_env, get_cluster_id, md5_hash
from databricks.model_training.api.validation import SupportedDataFormats, validate_output_to, validate_path
from databricks.model_training.types.train_config import TrainTaskType

AGENT_EVAL_MAX_SAMPLES = 500


def _load_data_as_df(
    data_path: str,
    data_format: SupportedDataFormats,
    use_serverless: bool = False,
    cluster_id: Optional[str] = None,
) -> DataFrame:
    """
    Loads data from the specified path as a Spark DataFrame.

    Args:
        data_path (str): Path to the data to load
        data_format (SupportedDataFormats): Format of the data. Must be a format supported by Mosaic AI Model Training.
        use_serverless (bool): Whether to use serverless compute or not
        cluster_id (Optional[str]): Cluster ID to use (required if not using serverless)

    Returns:
        DataFrame: A PySpark DataFrame representing the loaded data
    """
    if not use_serverless and not cluster_id:
        raise ValueError('cluster_id is required when not using serverless.')
    if use_serverless and cluster_id:
        raise ValueError('cluster_id provided while use_serverless specified. Please provide only one.')

    host, token = _get_host_and_token_from_env()

    try:
        if use_serverless:
            session_id = str(uuid4())
            spark = DatabricksSession.builder.host(host).token(token).header('x-databricks-session-id',
                                                                             session_id).getOrCreate()
        else:
            spark = DatabricksSession.builder.remote(host=host, token=token, cluster_id=cluster_id).getOrCreate()
    except Exception as e:
        raise RuntimeError(f'Failed to connect to Databricks: {str(e)}') from e

    try:
        if data_format == SupportedDataFormats.DELTA_TABLE:
            df = spark.table(data_path)
        elif data_format == SupportedDataFormats.UC_VOLUME:
            df = spark.read.json(data_path)
        elif data_format == SupportedDataFormats.HF_DATASET:
            dataset = hf_datasets.load_dataset(data_path)
            pd_df = pd.DataFrame(dataset)  # type: ignore
            df = spark.createDataFrame(pd_df)
        else:
            raise ValueError(f'Unsupported data format: {data_format}')
        return df
    except Exception as e:
        spark.stop()  # clean up the Spark session if there's an error
        raise RuntimeError(f"Failed to load '{data_path}': {str(e)}") from e


def _validate_and_load_data_as_df(
    data_path: str,
    data_path_type: str,
    use_serverless: bool = False,
    cluster_id: Optional[str] = None,
) -> DataFrame:
    """
    Validate the data path and load the data as a DataFrame.

    Args:
        data_path (str): Path to the data to load
        data_path_type (str): Type of data path (e.g., "train_data_path", "eval_data_path"). Used for error messages.
        use_serverless (bool): Whether to use serverless compute or not
        cluster_id (Optional[str]): Cluster ID to use (required if not using serverless)

    Returns:
        DataFrame: A PySpark DataFrame representing the loaded data
    """
    # Not supporting CPT evals. No difference between IFT/CHAT validation so we skip prompting task_type as an arg
    data_format = validate_path(data_path, TrainTaskType.INSTRUCTION_FINETUNE, data_path_type)
    df = _load_data_as_df(data_path, data_format, use_serverless, cluster_id)
    return df


def load_eval_set_as_df(eval_data_path: str,) -> DataFrame:
    """
    Loads the evaluation dataset as a Spark DataFrame.

    Args:
        eval_data_path (str): Path to the evaluation dataset. The format should be supported by Mosaic AI Training.

    Returns:
        DataFrame: A PySpark DataFrame representing the loaded evaluation data
    """
    # to associate Agent Eval billing with finetuning
    os.environ['RAG_EVAL_EVAL_SESSION_CLIENT_NAME'] = 'finetuning_eval'

    df = _validate_and_load_data_as_df(eval_data_path, 'eval_data_path', cluster_id=get_cluster_id())

    num_samples = df.count()
    if num_samples > AGENT_EVAL_MAX_SAMPLES:
        print(f'Dataset contains {num_samples} samples, ' \
              f'which exceeds the maximum allowed value of {AGENT_EVAL_MAX_SAMPLES}. ' \
              f'Truncating to {AGENT_EVAL_MAX_SAMPLES}.')
        df = df.limit(AGENT_EVAL_MAX_SAMPLES)
    return df


def split_eval_set(
    train_data_path: str,
    output_to: str,
    eval_split_ratio: float = 0.1,
    max_eval_samples: int = 500,
    seed: Optional[int] = None,
    use_serverless: bool = False,
) -> Tuple[str, str]:
    """
    Splits the dataset into training and evaluation sets. Writes the splits to new Delta tables.

    Args:
        train_data_path (str): Path to the training dataset. The format should be supported by Mosaic AI Training.
        output_to (str): Path to save the training and evaluation splits. This should be in the format 'schema.catalog'.
        eval_split_ratio (float): Ratio of the dataset to use for evaluation. The remainder will be used for training
        max_eval_samples (int): Maximum number of samples to include in the eval set.
        seed (int): Random seed for splitting the dataset
    """
    validate_output_to(output_to)
    if not 0 < eval_split_ratio < 1:
        raise ValueError('eval_split_ratio must be between 0 and 1.')
    if max_eval_samples <= 0:
        raise ValueError(f'max_eval_samples must be a positive integer, got {max_eval_samples}.')
    if max_eval_samples > AGENT_EVAL_MAX_SAMPLES:
        print(
            'max_eval_samples exceeds the maximum allowed value of ' \
            f'{AGENT_EVAL_MAX_SAMPLES}. Setting to {AGENT_EVAL_MAX_SAMPLES}.'
        )
        max_eval_samples = AGENT_EVAL_MAX_SAMPLES

    cluster_id = get_cluster_id() if not use_serverless else None

    # Databricks Default Storage requires serverless compute
    spark_df = _validate_and_load_data_as_df(train_data_path, 'train_data_path', use_serverless, cluster_id)

    total_rows = spark_df.count()
    batch_size = 1 << 30
    num_partitions = max(1, total_rows // batch_size)
    spark_df = spark_df.repartition(num_partitions)

    eval_samples = min(int(total_rows * eval_split_ratio), max_eval_samples)
    eval_df, train_df = spark_df.randomSplit([eval_samples, total_rows - eval_samples], seed=seed)

    # just in case something weird happens with Spark under the hood - ensure user can continue
    eval_df = eval_df.limit(max_eval_samples)

    print(
        f'Split {total_rows} samples into {total_rows - eval_df.count()} train samples ' \
        f'and {eval_df.count()} eval samples. Saving to {output_to}.'
    )

    train_table_path = f'{output_to}.train_split_{md5_hash(train_data_path)}'
    eval_table_path = f'{output_to}.eval_split_{md5_hash(train_data_path)}'

    train_df.write.format('delta').saveAsTable(train_table_path)
    eval_df.write.format('delta').saveAsTable(eval_table_path)

    print(f'Saved train data to {train_table_path} and eval data to {eval_table_path}.')

    return train_table_path, eval_table_path
