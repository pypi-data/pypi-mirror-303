"""API Response Models."""

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import StrEnum, auto
from zoneinfo import ZoneInfo

from mashumaro import field_options
from mashumaro.mixins.json import DataClassDictMixin


class RateBands(StrEnum):
    """Rate bands provided by Hydro Ottawa."""

    TIER_1 = auto()
    TIER_2 = auto()
    TIERED = "TIERED"


class AggregateType(StrEnum):
    """Enum for specifying the granularity of usage."""

    HOURLY = auto()
    DAILY = auto()
    MONTHLY = auto()


@dataclass(slots=True)
class HourlyRead(DataClassDictMixin):
    """Measurement by hour."""

    start_time: datetime = field(
        metadata=field_options(
            alias="startDateTime",
            deserialize=lambda d: datetime.fromisoformat(d).replace(
                tzinfo=ZoneInfo("America/Toronto"),
            ),
        ),
    )
    end_time: datetime = field(
        metadata=field_options(
            alias="endDateTime",
            deserialize=lambda d: datetime.fromisoformat(d).replace(
                tzinfo=ZoneInfo("America/Toronto"),
            ),
        ),
    )
    rate_band: str = field(metadata=field_options(alias="rateBand"))
    usage: float = field(metadata=field_options(alias="hourlyUsage"))
    cost: float = field(metadata=field_options(alias="hourlyCost"))


@dataclass(slots=True)
class HourlySummary(DataClassDictMixin):
    """Aggregate information for an hour."""

    account_id: str = field(metadata=field_options(alias="accountId"))
    actual_date: date = field(metadata=field_options(alias="actualDate"))
    rate_plan: str = field(metadata=field_options(alias="ratePlan"))
    billing_period_start_date: datetime = field(
        metadata=field_options(alias="billingPeriodStartDate"),
    )
    billing_period_end_date: datetime = field(
        metadata=field_options(alias="billingPeriodEndDate"),
    )
    total_usage: float = field(metadata=field_options(alias="totalUsage"))
    total_cost: float = field(metadata=field_options(alias="totalCost"))
    hourly_average_usage: float = field(
        metadata=field_options(alias="hourlyAverageUsage"),
    )
    hourly_average_cost: float = field(
        metadata=field_options(alias="hourlyAverageCost"),
    )
    total_off_peak_usage: float = field(
        metadata=field_options(alias="totalOffPeakUsage"),
    )
    total_off_peak_cost: float = field(metadata=field_options(alias="totalOffPeakCost"))
    total_mid_peak_usage: float = field(
        metadata=field_options(alias="totalMidPeakUsage"),
    )
    total_mid_peak_cost: float = field(metadata=field_options(alias="totalMidPeakCost"))
    total_on_peak_usage: float = field(metadata=field_options(alias="totalOnPeakUsage"))
    total_on_peak_cost: float = field(metadata=field_options(alias="totalOnPeakCost"))
    total_ulo_peak_usage: float = field(metadata=field_options(alias="totalUloUsage"))
    total_ulo_peak_cost: float = field(metadata=field_options(alias="totalUloCost"))
    number_of_hours: int = field(metadata=field_options(alias="numberOfHours"))


@dataclass(slots=True)
class HourlyResponse(DataClassDictMixin):
    """API response for /hourly."""

    summary: HourlySummary = field(metadata=field_options(alias="summary"))
    measurements: list[HourlyRead] = field(metadata=field_options(alias="intervals"))


@dataclass(slots=True)
class DailyRead(DataClassDictMixin):
    """Measurement by days. Billing Periods include more detail."""

    measurement_time: date = field(metadata=field_options(alias="date"))
    usage: float = field(metadata=field_options(alias="dailyUsage"))


@dataclass(slots=True)
class MonthlyRead(DataClassDictMixin):
    """Measurements by month."""

    start_date: date = field(metadata=field_options(alias="startDate"))
    end_date: date = field(metadata=field_options(alias="startDate"))
    monthly_usage: int = field(metadata=field_options(alias="monthlyUsage"))
    off_peak_usage: int = field(metadata=field_options(alias="offPeakUsage"))
    mid_peak_usage: int = field(metadata=field_options(alias="midPeakUsage"))
    on_peak_usage: int = field(metadata=field_options(alias="onPeakUsage"))
    ulo_usage: int = field(metadata=field_options(alias="uloUsage"))
    monthly_cost: float = field(metadata=field_options(alias="monthlyCost"))
    off_peak_cost: float = field(metadata=field_options(alias="offPeakCost"))
    mid_peak_cost: float = field(metadata=field_options(alias="midPeakUsage"))
    on_peak_cost: float = field(metadata=field_options(alias="onPeakCost"))
    ulo_cost: float = field(metadata=field_options(alias="uloCost"))
    rate_plan: str = field(metadata=field_options(alias="ratePlan"))


@dataclass(slots=True)
class BillingPeriodMeta(DataClassDictMixin):
    """Information about a billing period."""

    start_date: date = field(metadata=field_options(alias="startDate"))
    end_date: date = field(metadata=field_options(alias="endDate"))
    rate_plan: RateBands = field(metadata=field_options(alias="ratePlan"))
    current_billing_period: bool = field(
        metadata=field_options(alias="currentBillingPeriod"),
    )


@dataclass(slots=True)
class BillingPeriodSummary(DataClassDictMixin):
    """Aggregate information for a billing period."""

    account_id: str = field(metadata=field_options(alias="accountId"))
    actual_start_date: date = field(metadata=field_options(alias="actualStartDate"))
    actual_end_date: date = field(metadata=field_options(alias="actualEndDate"))
    rate_plan: str = field(metadata=field_options(alias="ratePlan"))
    total_usage: float = field(metadata=field_options(alias="totalUsage"))
    total_cost: float = field(metadata=field_options(alias="totalCost"))
    daily_average_usage: float = field(
        metadata=field_options(alias="dailyAverageUsage"),
    )
    daily_average_cost: float = field(
        metadata=field_options(alias="dailyAverageCost"),
    )
    total_off_peak_usage: float = field(
        metadata=field_options(alias="totalOffPeakUsage"),
    )
    total_off_peak_cost: float = field(metadata=field_options(alias="totalOffPeakCost"))
    total_mid_peak_usage: float = field(
        metadata=field_options(alias="totalMidPeakUsage"),
    )
    total_mid_peak_cost: float = field(metadata=field_options(alias="totalMidPeakCost"))
    total_on_peak_usage: float = field(metadata=field_options(alias="totalOnPeakUsage"))
    total_on_peak_cost: float = field(metadata=field_options(alias="totalOnPeakCost"))
    total_ulo_peak_usage: float = field(metadata=field_options(alias="totalUloUsage"))
    total_ulo_peak_cost: float = field(metadata=field_options(alias="totalUloCost"))
    number_of_days: int = field(metadata=field_options(alias="numberOfDays"))


@dataclass(slots=True)
class BillingPeriodRead(DataClassDictMixin):
    """Daily Measurement provided in Billing Period."""

    measurement_date: date = field(metadata=field_options(alias="date"))
    daily_usage: int = field(metadata=field_options(alias="dailyUsage"))
    off_peak_usage: int = field(metadata=field_options(alias="offPeakUsage"))
    mid_peak_usage: int = field(metadata=field_options(alias="midPeakUsage"))
    on_peak_usage: int = field(metadata=field_options(alias="onPeakUsage"))
    ulo_usage: int = field(metadata=field_options(alias="uloUsage"))
    daily_usage_cost: float = field(metadata=field_options(alias="dailyCost"))
    off_peak_cost: float = field(metadata=field_options(alias="offPeakCost"))
    mid_peak_cost: float = field(metadata=field_options(alias="midPeakUsage"))
    on_peak_cost: float = field(metadata=field_options(alias="onPeakCost"))
    ulo_cost: float = field(metadata=field_options(alias="uloCost"))


@dataclass(slots=True)
class BillRead(DataClassDictMixin):
    """Response returned by /billing-period."""

    summary: BillingPeriodSummary
    intervals: list[BillingPeriodRead]
