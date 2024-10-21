"""Asynchronous Python client for the Hydro Ottawa API."""

import asyncio
import logging
from datetime import date, datetime, timedelta
from itertools import chain
from typing import ClassVar, Literal, overload
from zoneinfo import ZoneInfo

import aiohttp
import boto3
from aiohttp.client_exceptions import ClientResponseError

from .aws_srp import AWSSRP
from .exceptions import HydroOttawaConnectionError, HydroOttawaInvalidAuthError
from .models import (
    AggregateType,
    BillingPeriodMeta,
    BillRead,
    DailyRead,
    HourlyRead,
    HourlyResponse,
    MonthlyRead,
)

logger = logging.getLogger(__name__)
DEBUG_LOG_RESPONSE = False


class HydroOttawa:
    """Class that can get historical and forecasted usage/cost from Bidgely's NA API."""

    BASE_URL: ClassVar[str] = "https://api-myaccount.hydroottawa.com"

    def __init__(
        self,
        session: aiohttp.ClientSession,
        username: str,
        password: str,
    ) -> None:
        """Create a Hydro Ottawa client given a username and password."""
        self.session: aiohttp.ClientSession = session
        self.username: str = username
        self.password: str = password
        self.x_access: str | None = None
        self.x_id: str | None = None
        self.auth_token: str | None = None

    async def async_login(self) -> None:
        """Return user-id and token for Bidgely."""
        client = await asyncio.get_running_loop().run_in_executor(
            None,
            boto3.client,
            "cognito-idp",
            "ca-central-1",
        )
        aws = AWSSRP(
            username=self.username,
            password=self.password,
            pool_id="ca-central-1_VYnwOhMBK",
            client_id="7scfcis6ecucktmp4aqi1jk6cb",
            client=client,
            loop=self.session.loop,
        )
        try:
            tokens = await aws.authenticate_user()
            self.x_access = tokens["AuthenticationResult"]["AccessToken"]
            self.x_id = tokens["AuthenticationResult"]["IdToken"]

            headers = {"x-id": self.x_id, "x-access": self.x_access}

            async with self.session.get(
                f"{self.BASE_URL}/app-token",
                headers=headers,
            ) as resp:
                self.auth_token = resp.headers["x-amzn-remapped-authorization"]
        except ClientResponseError as err:
            if err.status in (401, 403):
                raise HydroOttawaInvalidAuthError from err
            raise HydroOttawaConnectionError from err

    async def fetch_hourly(self, fetch_date: date | None = None) -> list[HourlyRead]:
        """Fetch hourly readings."""
        if fetch_date is None:
            fetch_date = datetime.now(ZoneInfo("America/Toronto")) - timedelta(days=1)
            fetch_date = fetch_date.date()
        url = f"{self.BASE_URL}/usage/consumption/hourly"
        headers = {
            "x-id": self.x_id,
            "x-access": self.x_access,
            "Authorization": self.auth_token,
        }
        async with self.session.post(
            url,
            headers=headers,
            json={"date": f"{fetch_date}"},
        ) as resp:
            reads = await resp.json()
            total = HourlyResponse.from_dict(reads)

        return total.measurements

    async def fetch_daily(
        self,
        start_date: date | None = None,
        end_date: date | None = None,
    ) -> list[DailyRead]:
        """Fetch measurements at daily granularity."""
        if start_date is None:
            start_date = datetime.now(ZoneInfo("America/Toronto")) - timedelta(days=8)
            start_date = start_date.date()
        if end_date is None:
            end_date = datetime.now(ZoneInfo("America/Toronto")).date() - timedelta(
                days=1,
            )
        url = f"{self.BASE_URL}/usage/consumption/daily"
        headers = {
            "x-id": self.x_id,
            "x-access": self.x_access,
            "Authorization": self.auth_token,
        }
        async with self.session.post(
            url,
            headers=headers,
            json={"startDate": f"{start_date}", "endDate": f"{end_date}"},
        ) as resp:
            reads = await resp.json()

        return [DailyRead.from_dict(read) for read in reads["intervals"]]

    async def fetch_monthly(
        self,
        start_date: date | None = None,
        end_date: date | None = None,
    ) -> list[MonthlyRead]:
        """Fetch measurements at a monthly granularity."""
        if start_date is None:
            start_date = datetime.now(ZoneInfo("America/Toronto")) - timedelta(days=365)
            start_date = start_date.date()
        if end_date is None:
            end_date = datetime.now(ZoneInfo("America/Toronto")).date() - timedelta(
                days=1,
            )
        url = f"{self.BASE_URL}/usage/consumption/monthly"
        headers = {
            "x-id": self.x_id,
            "x-access": self.x_access,
            "Authorization": self.auth_token,
        }
        async with self.session.post(
            url,
            headers=headers,
            json={"startDate": f"{start_date}", "endDate": f"{end_date}"},
        ) as resp:
            reads = await resp.json()

        return [MonthlyRead.from_dict(read) for read in reads["intervals"]]

    async def fetch_billing_period(self, start_date: date, end_date: date) -> BillRead:
        """Get information about a single billing period."""
        headers = {
            "x-id": self.x_id,
            "x-access": self.x_access,
            "Authorization": self.auth_token,
        }
        async with self.session.post(
            f"{self.BASE_URL}/usage/consumption/billing-period",
            headers=headers,
            json={"startDate": f"{start_date}", "endDate": f"{end_date}"},
        ) as resp:
            reads = await resp.json()

        return BillRead.from_dict(reads)

    async def get_billing_periods(self) -> list[BillingPeriodMeta]:
        """Return a list of billing periods without measurements."""
        headers = {
            "x-id": self.x_id,
            "x-access": self.x_access,
            "Authorization": self.auth_token,
        }
        async with self.session.get(
            f"{self.BASE_URL}/usage/billing-period-list",
            headers=headers,
        ) as resp:
            reads = await resp.json()

        return [BillingPeriodMeta.from_dict(period) for period in reads]

    @overload
    async def get_usage(
        self,
        start_date: date | None,
        end_date: date | None,
        aggregate: Literal[AggregateType.HOURLY],
    ) -> list[HourlyRead]: ...

    @overload
    async def get_usage(
        self,
        start_date: date | None,
        end_date: date | None,
        aggregate: Literal[AggregateType.DAILY],
    ) -> list[DailyRead]: ...

    @overload
    async def get_usage(
        self,
        start_date: date | None,
        end_date: date | None,
        aggregate: Literal[AggregateType.MONTHLY],
    ) -> list[MonthlyRead]: ...

    async def get_usage(
        self,
        start_date: date | None = None,
        end_date: date | None = None,
        aggregate: AggregateType = AggregateType.HOURLY,
    ):
        """Get usage with a granularity specified by aggregate."""
        if start_date is None:
            start_date = datetime.now(ZoneInfo("America/Toronto")) - timedelta(days=8)
            start_date = start_date.date()
        if end_date is None:
            end_date = datetime.now(ZoneInfo("America/Toronto")).date() - timedelta(
                days=1,
            )

        match aggregate:
            case AggregateType.HOURLY:
                tasks = []
                days = (
                    start_date + timedelta(days=x)
                    for x in range((end_date - start_date).days + 1)
                )
                for day in days:
                    single_day = self.fetch_hourly(day)
                    tasks.append(single_day)
                result = await asyncio.gather(*tasks)
                hourlies: list[HourlyRead] = list(chain.from_iterable(result))
                return hourlies
            case AggregateType.DAILY:
                return await self.fetch_daily(start_date, end_date)
            case AggregateType.MONTHLY:
                logger.error("Monthly readings are not supported yet.")
                monthlies: list[MonthlyRead] = []
                return monthlies
