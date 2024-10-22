""" Common models
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Generic, Iterator, List, TypeVar

from .utils import create_horizontal_html_table, create_vertical_html_table

O = TypeVar('O', bound=type(dataclass))


class ObjectType(Enum):
    """ Enum for Types of Objects Allowed """

    TRAINING_RUN = 'training_run'
    SWEEP = 'sweep'
    TRAINING_EVENT = 'training_event'
    RUN_EVENT = 'run_event'
    TRAINING_MODEL_CONSTANTS = 'training_model_constants'
    TRAINING_CONSTANTS = 'training_constants'

    UNKNOWN = 'unknown'

    def _get_display_columns(self) -> Dict[str, str]:
        """
        This is currently used only for html display (inside a notebook)

        Ideally the CLI & notebook display will be unified

        Returns:
            Dict[str, str]: Mapping of class column name to display name
        """

        if self == ObjectType.TRAINING_RUN:
            display_columns = {
                '_mlflow_run_link_html': 'Name',
                'run_progress': 'Status',
                '_mlflow_experiment_link_html': 'MLflow Experiment ID',
                'model': 'Model',
                'learning_rate': 'Learning Rate',
                'training_duration': 'Training Duration',
                'train_data_path': 'Train Data Path',
                'register_to': 'Register To',
            }
            return display_columns

        if self == ObjectType.SWEEP:
            display_columns = {
                '_mlflow_experiment_link_html': 'MLflow Experiment ID',
                '_created_at_str': 'Created At',
                '_sweep_status_str': 'Status',
                '_sweep_finetune_table': 'Runs',
            }
            return display_columns

        if self == ObjectType.TRAINING_EVENT:
            return {
                'type': 'Type',
                'time': 'Time',
                'message': 'Message',
            }

        if self == ObjectType.TRAINING_MODEL_CONSTANTS:
            return {'display_name': 'Model Name', 'name': 'Input Name', 'max_context_length': 'Maximum Context Length'}

        return {}

    @classmethod
    def from_model_type(cls, model) -> ObjectType:
        # pylint: disable-next=import-outside-toplevel
        from databricks.model_training.types.sweep import Sweep
        # pylint: disable-next=import-outside-toplevel
        from databricks.model_training.types.training_constants import TrainingConstants, TrainingModelConstants
        # pylint: disable-next=import-outside-toplevel
        from databricks.model_training.types.training_run import RunEvent, TrainingEvent, TrainingRun
        if model == TrainingRun:
            return ObjectType.TRAINING_RUN
        if model == Sweep:
            return ObjectType.SWEEP
        if model == TrainingEvent:
            return ObjectType.TRAINING_EVENT
        if model == RunEvent:
            return ObjectType.RUN_EVENT
        if model == TrainingModelConstants:
            return ObjectType.TRAINING_MODEL_CONSTANTS
        if model == TrainingConstants:
            return ObjectType.TRAINING_CONSTANTS
        return ObjectType.UNKNOWN


def generate_html_table(data: List[O], attr_to_label: Dict[str, str]) -> str:
    """
    Parameters
    ----------
    data : List[O]
        List of objects
    attr_to_label : dict
        Mapping of attributes (of the object) to labels/table headers

    Returns
    -------
    str
        An HTML table as a string. The top row will be a header consisting
        of the provided labels, and every other row will correspond to the
        provided objects
    """
    table_data = [{attr: getattr(obj, attr, None) for attr in attr_to_label} for obj in data]
    return create_horizontal_html_table(table_data, attr_to_label)


def generate_vertical_html_table(data: List[O], attr_to_label: Dict[str, str]) -> str:
    """
    Parameters
    ----------
    data : List[O]
        List of objects
    attr_to_label : dict
        Mapping of attributes (of the object) to labels/table headers

    Returns
    -------
    str
        An HTML table as a string. The leftmost column will be the headers provided
        as attr labels. The remaining columns will be the attributes of the objects.
    """
    table_data = [{attr: getattr(obj, attr, None) for attr in attr_to_label} for obj in data]
    return create_vertical_html_table(table_data, attr_to_label)


class ObjectList(Generic[O]):
    """Common helper for list of objects
    """

    def __init__(self, data: List[O], obj_type: ObjectType):
        self.data = data
        self.type = obj_type

    def __repr__(self) -> str:
        return f'List{self.data}'

    def __iter__(self) -> Iterator[O]:
        return iter(self.data)

    def __getitem__(self, index: int):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def insert(self, index, item):
        self.data.insert(index, item)

    def append(self, item):
        self.data.append(item)

    def extend(self, item):
        self.data.extend(item)

    def __len__(self) -> int:
        return len(self.data)

    @property
    def display_columns(self) -> Dict[str, str]:
        return self.type._get_display_columns()  # pylint: disable=protected-access

    def __str__(self):
        return '[' + ', '.join([str(i) for i in self.data]) + ']'

    def _repr_html_(self) -> str:
        return generate_html_table(self.data, self.display_columns)

    def to_pandas(self):
        try:
            # pylint: disable=import-outside-toplevel
            import pandas as pd  # type: ignore
        except ImportError as e:
            raise ImportError('Please install pandas to use this feature') from e

        cols = self.display_columns
        res = {col: [] for col in cols}
        for row in self.data:
            for col in cols:
                value = getattr(row, col)
                res[col].append(value if value else '')

        return pd.DataFrame(data=res)
