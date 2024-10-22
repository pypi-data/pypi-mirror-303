"""
A Databricks sweep.
"""
import logging
from dataclasses import dataclass
from datetime import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Tuple

from mcli import MAPIException
from mcli.api.schema.generic_model import DeserializableModel, convert_datetime
from mcli.utils.utils_string_functions import camel_case_to_snake_case

from databricks.model_training.types.sweep_status import SweepStatus

from .training_run import TrainingRun
from .utils import create_horizontal_html_table, get_mlflow_experiment_link_html, get_mlflow_run_link_html

logger = logging.getLogger(__name__)


@dataclass()
class Sweep(DeserializableModel):
    """A Databricks sweep object.

        Args:
            mlflow_experiment_id (str): The MLflow experiment ID.
            created_at (datetime): The timestamp when the sweep was created.
            sweep_status (SweepStatus): The status of the sweep.
            finetunes (List[Finetune]): The list of Finetune runs.
            reason (Optional[str], optional): The optional reason to expand on the sweep status. Defaults to None.
    """
    mlflow_experiment_id: str
    created_at: datetime
    sweep_status: SweepStatus
    finetunes: List[TrainingRun]
    reason: Optional[str] = None

    _required_properties: Tuple[str, ...] = tuple([
        'mlflowExperimentId',
        'createdAt',
        'sweepStatus',
        'finetunes',
    ])

    @classmethod
    def from_mapi_response(cls, response: Dict[str, Any]) -> 'Sweep':
        """Load the sweep from MAPI response."""
        missing = set(cls._required_properties) - set(response.keys())
        if missing:
            raise MAPIException(status=HTTPStatus.BAD_REQUEST,
                                message='Missing required key(s) in response to deserialize Sweep '
                                f'object: {", ".join(missing)}')
        args = {camel_case_to_snake_case(key): value for key, value in response.items()}
        return cls(
            mlflow_experiment_id=args['mlflow_experiment_id'],
            created_at=convert_datetime(args['created_at']),
            sweep_status=SweepStatus.from_string(args['sweep_status']),
            reason=args['reason'] if 'reason' in args else None,
            finetunes=[TrainingRun.from_mapi_response(finetune) for finetune in args['finetunes']],
        )

    def __iter__(self):
        """Iterate over finetunes."""
        return iter(self.finetunes)

    @property
    def _sweep_status_str(self) -> str:
        """Get the sweep status as a string.
        """
        if self.reason:
            return f'{self.sweep_status} ({self.reason})'
        return str(self.sweep_status)

    @property
    def _mlflow_experiment_link_html(self) -> str:
        """
        Get a hyperlinked experiment ID.
        This link will open the MLflow experiment page in a new tab.

        Raises:
            ValueError: If the experiment ID is not set
        """
        if self.mlflow_experiment_id is None:
            raise ValueError('Experiment ID is not set')
        return get_mlflow_experiment_link_html(self.mlflow_experiment_id, self.mlflow_experiment_id)

    @property
    def _created_at_str(self) -> str:
        """Get the created at as a string.
        """
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')

    @property
    def _sweep_finetune_table(self):
        """Display table with sweep finetunes."""
        pruned_finetunes = []
        for finetune in self.finetunes:
            pruned_finetunes.append({
                'name': get_mlflow_run_link_html(self.mlflow_experiment_id, finetune.run_id, finetune.name),
                'status': finetune.status,
                'training_duration': finetune.training_duration,
                'learning_rate': finetune.learning_rate,
            })
        sorted_finetunes = sorted(pruned_finetunes, key=lambda x: (x['training_duration'], x['learning_rate']))
        key_to_label = {key: ' '.join([word.title() for word in key.split('_')]) for key in pruned_finetunes[0].keys()}
        return create_horizontal_html_table(sorted_finetunes, key_to_label)

    def _repr_html_(self) -> str:
        """Display the sweep as HTML.
            """
        data = {
            'mlflow_experiment_id': self._mlflow_experiment_link_html,
            'created_at': self._created_at_str,
            'status': self._sweep_status_str,
            'runs': self._sweep_finetune_table
        }
        key_to_label = {key: key.replace('_', ' ').title() for key in data}
        return create_horizontal_html_table([data], key_to_label)
