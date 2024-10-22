"""Contants for pymymeter."""

from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import StrEnum


@dataclass
class UsageRead:
    """Power Usage Data."""

    start_time: datetime
    end_time: datetime
    consumption: float
    unit_of_measurement: str


@dataclass
class CostRead:
    """Cost Usage Data."""

    start_time: datetime
    end_time: datetime
    provided_cost: float


class UsageInterval(StrEnum):
    """Options for data interval."""

    MINUTE15 = "3"
    MINUTE30 = "4"
    HOUR = "5"
    DAY = "6"
    WEEK = "8"
    MONTH = "9"
    BILL = "7"

    def to_timedelta(self) -> timedelta:
        """Convert the interval to a timedelta object."""
        time_intervals = {
            UsageInterval.MINUTE15: timedelta(minutes=15),
            UsageInterval.MINUTE30: timedelta(minutes=30),
            UsageInterval.HOUR: timedelta(hours=1),
            UsageInterval.DAY: timedelta(days=1),
            UsageInterval.WEEK: timedelta(weeks=1),
            UsageInterval.MONTH: timedelta(days=30),
            UsageInterval.BILL: timedelta(days=30),
        }
        return time_intervals[self]


class UsageType(StrEnum):
    """Options for usage type."""

    COST = "3"
    CONSUMPTION = "1"
