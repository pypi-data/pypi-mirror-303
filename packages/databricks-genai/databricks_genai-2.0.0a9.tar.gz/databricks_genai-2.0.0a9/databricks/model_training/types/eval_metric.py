"""Utilities for logging evaluation metrics"""

from typing import Optional, TypedDict


class EvalMetricDict(TypedDict):
    metric_name: str
    score: float
    greater_is_better: bool
    baseline_score: Optional[float]
