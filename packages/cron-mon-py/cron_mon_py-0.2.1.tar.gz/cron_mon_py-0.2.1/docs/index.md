[CronMon](https://github.com/cron-mon-io)'s Python SDK, making Python cron job monitoring simple.

## Installation

`cron-mon-py` can be installed via `pip` - or your Python package manager of choice - like any other Python package you might install

```console
pip install cron-mon-py
```

## Monitor setup

Before you can start monitoring a cron job, you'll need to have [CronMon](https://github.com/cron-mon-io) itself deployed and running.

!!! note

    Cron Mon consists of a backend service, [`cron-mon`](https://github.com/cron-mon-io/cron-mon), and a frontend application, [`cron-mon-app`](https://github.com/cron-mon-io/cron-mon-app). Both need to be deployed separately, but there are Docker images available on GitHub Container Registry, at `ghcr.io/cron-mon-io/cron-mon` and `ghcr.io/cron-mon-io/cron-mon-app`, respectively. For full deployment guidelines on both, see their respective GitHub repositories.

From here, you just need to create a _Monitor_ for your cron job/ scheduled task, as well as an API key - both of which are very quick and simple to do and is documented within Cron Mon itself, but it is not documented here to avoid duplication.

## Usage

When you get to this point, you're ready to make the necessary changes to your cron job/ scheduled task to start monitoring it.

Firstly, you need to provide 2 environment variables to the process that runs your job - these are:

1. `CRON_MON_SERVER_URL`: The base URL for where you have `cron-mon` deployed and running.
2. `CRON_MON_API_KEY`: The API key for `cron-mon-py` to use when monitoring.
 
From here, you just need to add 2 lines of code to your cron job:

```py hl_lines="1-2 4-6"
# Import the `monitor` decorator from `cron_mon`
from cron_mon import monitor

# Decorate the function that serves as the entry point for your cron job.
# Note that <monitor-id> needs to be replaced with the ID of your monitor.
@monitor("<monitor-id>")
def cron_job() -> None:
    """A cron job."""
    # Cron job code here.
```

From here, whenever `cron_job` is called, the time at which it starts and ends will be recorded in your instance of Cron Mon, as well as if any unhandled exceptions occured, and any (textual) output.

!!! note

    Your cron job function can have parameters.

### Error handling

Exceptions that are not caught by `cron_job` in the above example will be caught by the `monitor` decorator, in order for details on that exception to be recorded and that job marked as a failure, but they will be re-raised, effectively meaning that there's no affect on the behaviour of the code being monitored.

`cron-mon-py` effectively treats any job which didn't raise an exception as succeeded. If you wish handle certain exceptions in some way but still have their occurance mark the job as a failure, this can be achieved by wrapping your cron job function in another which performs that error handling:

```py
from cron_mon import monitor

@monitor("<monitor-id>")
def cron_job_inner() -> None:
    """This is the code that CronMon will monitor, which may raise a FooException."""

def cron_job() -> None:
    """This is the cron job."""
    try:
        cron_job_inner()
    except FooException:
        # Handle the exception as required.
```
