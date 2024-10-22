import datetime
from datetime import date
from typing import Any, Optional, Union

import pydantic
from pydantic import BaseModel, ConfigDict, Field
from pydantic_core.core_schema import ValidationInfo

from classiq.interface.enum_utils import StrEnum


class Granularity(StrEnum):
    monthly = "MONTHLY"
    daily = "DAILY"
    hourly = "HOURLY"


class CostScope(StrEnum):
    user = "user"
    organization = "organization"


class ExecutionCostForTimePeriod(BaseModel):
    start: date = Field(
        description="The beginning of the time period for tasks usage and cost (inclusive)."
    )
    end: date = Field(
        description="The end of the time period for tasks usage and cost (exclusive)."
    )
    granularity: Granularity = Field(
        description="Either MONTHLY or DAILY, or HOURLY.", default=Granularity.daily
    )
    cost_scope: CostScope = Field(
        description="Either user or organization", default=CostScope.user
    )

    @pydantic.field_validator("start", mode="before")
    @classmethod
    def validate_start_date(cls, start_date: Union[datetime.datetime, date]) -> date:
        if isinstance(start_date, datetime.datetime):
            return start_date.date()
        return start_date

    @pydantic.field_validator("end", mode="before")
    @classmethod
    def validate_date_and_date_order(
        cls, v: Union[date, datetime.datetime], info: ValidationInfo
    ) -> date:
        if isinstance(v, datetime.datetime):
            v = v.date()
        if "start" in info.data and v <= info.data["start"]:
            raise ValueError('"end" date should be after "start" date')
        return v

    def dict(self, **kwargs: Any) -> dict[str, Any]:
        data = super().model_dump(**kwargs)
        data["start"] = self.start.strftime("%Y-%m-%d")
        data["end"] = self.end.strftime("%Y-%m-%d")
        return data


"""The following models describe the aws response model and based on this schema:
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_cost_and_usage"""


class TimePeriod(pydantic.BaseModel):
    Start: str
    End: str


class BlendedCost(pydantic.BaseModel):
    Amount: str
    Unit: str


class Total(pydantic.BaseModel):
    BlendedCost: BlendedCost


class ExecutedTaskForPeriodItem(pydantic.BaseModel):
    TimePeriod: TimePeriod
    Total: Total
    Groups: Optional[list] = None
    Estimated: Optional[bool] = None

    model_config = ConfigDict(extra="forbid")


class ExecutionCostForTimePeriodResponse(pydantic.BaseModel):
    executed_task_for_period: list[ExecutedTaskForPeriodItem]
