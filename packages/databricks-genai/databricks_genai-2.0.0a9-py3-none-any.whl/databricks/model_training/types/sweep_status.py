"""Sweep Status"""
from enum import Enum
from typing import Union

from mcli.utils.utils_string_functions import camel_case_to_snake_case, snake_case_to_camel_case

__all__ = ['SweepStatus']


class SweepStatus(Enum):
    """Possible statuses of a sweep
    """
    # If all runs in sweep are pending/queued
    PENDING = 'PENDING'

    # If at least one run in sweep has started training
    RUNNING = 'RUNNING'

    # User manually canceled a sweep or all runs in a sweep
    CANCELED = 'CANCELED'

    # There is 1+ failed run in sweep
    FAILED = 'FAILED'

    # If all runs in sweep are completed
    COMPLETED = 'COMPLETED'

    def __str__(self) -> str:
        return self.value

    @classmethod
    def from_string(cls, sweep_status: Union[str, 'SweepStatus']) -> 'SweepStatus':
        """Convert a string to a valid SweepStatus Enum

        If the sweep status string is not recognized, will return SweepStatus.FAILED
        instead of raising a KeyError
        """
        if isinstance(sweep_status, SweepStatus):
            return sweep_status

        default = SweepStatus.FAILED  # Defaulting to FAILED for unrecognized statuses
        try:
            key = camel_case_to_snake_case(sweep_status).upper()
            return cls[key]
        except TypeError:
            return default
        except KeyError:
            return default

    @property
    def display_name(self) -> str:
        return snake_case_to_camel_case(self.value, capitalize_first=True)
