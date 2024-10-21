"""Tests for the `monitor` decorator's error handling."""

import pytest
import responses
from responses import matchers

from cron_mon import CronMonAPIException, InvalidAPIKey, monitor
from tests.constants import API_FINISH_URL, API_START_URL, MONITOR_ID


def test_connection_errors() -> None:
    """Test that the `monitor` decorator handles connection errors."""

    @monitor(MONITOR_ID)
    def cron_job() -> str:
        """A sample cron job."""
        return "Hello, world!"

    with pytest.raises(CronMonAPIException):
        cron_job()


@responses.activate
def test_failed_start() -> None:
    """Test that the `monitor` decorator handles failed job starts."""
    responses.post(
        API_START_URL,
        status=500,
        json={
            "error": {
                "code": "500",
                "reason": "Internal Server Error",
                "description": "Failed to start job",
            }
        },
        match=[matchers.header_matcher({"X-API-Key": "mock-api-key"})],
    )

    @monitor(MONITOR_ID)
    def cron_job() -> str:
        """A sample cron job."""
        return "Hello, world!"

    with pytest.raises(CronMonAPIException) as exc:
        cron_job()

    assert str(exc.value) == "Failed to start job"


@responses.activate
def test_failed_finish() -> None:
    """Test that the `monitor` decorator handles failed job finishes."""
    responses.post(
        API_START_URL,
        json={"data": {"job_id": "12345"}},
        match=[matchers.header_matcher({"X-API-Key": "mock-api-key"})],
    )
    responses.post(
        API_FINISH_URL,
        status=500,
        json={
            "error": {
                "code": "500",
                "reason": "Internal Server Error",
                "description": "Failed to finish job",
            }
        },
        match=[matchers.header_matcher({"X-API-Key": "mock-api-key"})],
    )

    @monitor(MONITOR_ID)
    def cron_job() -> str:
        """A sample cron job."""
        return "Hello, world!"

    with pytest.raises(CronMonAPIException) as exc:
        cron_job()

    assert str(exc.value) == "Failed to finish job"


@responses.activate
def test_invalid_api_key() -> None:
    """Test that the `monitor` decorator handles failed job finishes with output."""
    responses.post(
        API_START_URL,
        status=401,
        json={
            "error": {
                "code": 401,
                "reason": "Unauthorized",
                "description": "Unauthorized: Invalid API key",
            }
        },
        match=[matchers.header_matcher({"X-API-Key": "mock-api-key"})],
    )

    @monitor(MONITOR_ID)
    def cron_job() -> str:
        """A sample cron job."""
        return "Hello, world!"

    with pytest.raises(InvalidAPIKey) as exc:
        cron_job()

    assert str(exc.value) == "Unauthorized: Invalid API key"
