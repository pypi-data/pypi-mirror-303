"""Tests that ensure the `monitor` decorator takes its config from env."""

import os
import sys
from unittest import mock

import pytest


@pytest.mark.parametrize(
    ["env_vars", "error_message"],
    [
        ({}, "CRON_MON_SERVER_URL"),
        ({"CRON_MON_SERVER_URL": "http://localhost:8000"}, "CRON_MON_API_KEY"),
        ({"CRON_MON_API_KEY": "test"}, "CRON_MON_SERVER_URL"),
    ],
)
def test_monitor_env(env_vars: dict[str, str], error_message: str) -> None:
    """Test that the `monitor` decorator takes its config from env."""
    # when `cron_mon.monitor` is imported in other tests, it will be pre-loaded
    # with the default env vars. We need to remove it from `sys.modules` to
    # ensure it is re-imported with the new env vars in this test.
    sys.modules.pop("cron_mon.monitor", None)

    with mock.patch.dict(os.environ, env_vars, clear=True):
        with pytest.raises(KeyError, match=error_message):
            from cron_mon.monitor import monitor  # noqa: F401
