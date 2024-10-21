"""Asynchronous Python client for the Hydro Ottawa API."""

import logging

from .exceptions import (
    HydroOttawaConnectionError,
    HydroOttawaError,
    HydroOttawaInvalidAuthError,
)
from .hydro_ottawa import HydroOttawa
from .models import (
    AggregateType,
    BillingPeriodMeta,
    BillingPeriodRead,
    BillingPeriodSummary,
    BillRead,
    DailyRead,
    HourlyRead,
    MonthlyRead,
)

__all__ = [
    "AggregateType",
    "DailyRead",
    "HourlyRead",
    "HydroOttawa",
    "BillingPeriodMeta",
    "BillingPeriodRead",
    "BillingPeriodSummary",
    "BillRead",
    "MonthlyRead",
    "HydroOttawaError",
    "HydroOttawaConnectionError",
    "HydroOttawaInvalidAuthError",
]

logging.getLogger("hydro_ottawa").addHandler(logging.NullHandler())
