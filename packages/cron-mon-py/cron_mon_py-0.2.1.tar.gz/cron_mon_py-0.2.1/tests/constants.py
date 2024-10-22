"""Constants for tests."""

# Helpful constants for testing.
MONITOR_ID = "a04376e2-0fb5-4949-9744-7c5d0a50b411"
API_START_URL = (
    f"http://mock.cron-mon.io/api/v1/monitors/{MONITOR_ID}/jobs/start"
)
API_FINISH_URL = (
    f"http://mock.cron-mon.io/api/v1/monitors/{MONITOR_ID}/jobs/12345/finish"
)
