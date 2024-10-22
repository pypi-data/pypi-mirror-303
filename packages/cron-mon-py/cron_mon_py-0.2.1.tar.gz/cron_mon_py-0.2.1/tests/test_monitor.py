"""Basic tests for the `monitor` decorator on the 'happy path'."""

import pytest
import responses
from responses import matchers

from cron_mon import monitor
from tests.constants import API_FINISH_URL, API_START_URL, MONITOR_ID


@responses.activate
def test_monitoring() -> None:
    """Test that the `monitor` decorator works as expected."""
    responses.post(
        API_START_URL,
        json={"data": {"job_id": "12345"}},
        match=[matchers.header_matcher({"X-API-Key": "mock-api-key"})],
    )
    responses.post(
        API_FINISH_URL,
        json={"data": {}},
        match=[
            matchers.header_matcher({"X-API-Key": "mock-api-key"}),
            matchers.json_params_matcher(
                {"succeeded": True, "output": "Hello, world!"}
            ),
        ],
    )

    @monitor(MONITOR_ID)
    def cron_job() -> str:
        """A sample cron job."""
        return "Hello, world!"

    cron_job()

    assert [c.request.url for c in responses.calls] == [
        API_START_URL,
        API_FINISH_URL,
    ]


@responses.activate
def test_monitor_failing_job() -> None:
    """Test that the `monitor` decorator handles failing jobs."""
    responses.post(
        API_START_URL,
        json={"data": {"job_id": "12345"}},
        match=[matchers.header_matcher({"X-API-Key": "mock-api-key"})],
    )
    responses.post(
        API_FINISH_URL,
        json={"data": {}},
        match=[
            matchers.header_matcher({"X-API-Key": "mock-api-key"}),
            matchers.json_params_matcher(
                {"succeeded": False, "output": "Job failed"}
            ),
        ],
    )

    @monitor(MONITOR_ID)
    def cron_job() -> str:
        """A sample cron job."""
        raise ValueError("Job failed")

    # Any exceptions raised by the job should be propagated up to the caller.
    with pytest.raises(ValueError):
        cron_job()

    assert [c.request.url for c in responses.calls] == [
        API_START_URL,
        API_FINISH_URL,
    ]
