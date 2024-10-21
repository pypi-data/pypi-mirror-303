"""Decorator for monitoring function execution time via CronMon."""

import os
from functools import wraps
from typing import Any, Callable, Optional

from requests import ConnectionError, Session

from .exceptions import CronMonAPIException, InvalidAPIKey


class monitor:
    """A decorator class for monitoring function execution time via CronMon."""

    __SERVER_URL = os.environ["CRON_MON_SERVER_URL"]
    __API_KEY = os.environ["CRON_MON_API_KEY"]
    # TODO: Logger?

    def __init__(self, monitor_id: str) -> None:
        """Initialize the decorator with the monitor ID to use for monitoring.

        Args:
            monitor_id: The monitor ID to use for monitoring the function.
        """
        self.monitor_id = monitor_id

    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        """Wrap the function with monitoring logic.

        Args:
            func: The function to wrap with monitoring logic.
        """

        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict) -> Any:
            with Session() as session:
                job_id = self.__record_start(session)

                # Execute the decorated function and record the output and any
                # exceptions that occur.
                exc = None
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    exc = e

                output = exc or result
                self.__record_finish(
                    session,
                    job_id,
                    exc is None,
                    str(output) if output else None,
                )

                # Raise an exception if one occurred, since we don't want to
                # swallow exceptions, just record them. The underlying
                # application can decide if/ how to handle them.
                if exc:
                    raise exc

                return result

        return wrapper

    def __record_start(self, session: Session) -> str:
        """Record the start of a job with the CronMon server.

        Args:
            session: The session to use for making the API call.

        Returns:
            The job ID for the started job.
        """
        return self.__api_call(
            session, f"/monitors/{self.monitor_id}/jobs/start"
        )["job_id"]

    def __record_finish(
        self,
        session: Session,
        job_id: str,
        succeeded: bool,
        output: Optional[str],
    ) -> None:
        """Record the finish of a job with the CronMon server.

        Args:
            session: The session to use for making the API call.
            job_id: The job ID for the job to finish.
            succeeded: Whether the job succeeded or not.
            output: The output of the job.
        """
        self.__api_call(
            session,
            f"/monitors/{self.monitor_id}/jobs/{job_id}/finish",
            json={"succeeded": succeeded, "output": output},
        )

    def __api_call(
        self, session: Session, endpoint: str, json: Optional[dict] = None
    ) -> dict:
        """Make an API call to the CronMon server.

        Args:
            session: The session to use for making the API call.
            endpoint: The API endpoint to call.
            json: The JSON data to send with the API call.

        Returns:
            The JSON response from the API call.
        """
        try:
            response = session.post(
                url=f"{self.__SERVER_URL}/api/v1{endpoint}",
                headers={"X-API-Key": self.__API_KEY},
                json=json,
            )
        except ConnectionError as e:
            raise CronMonAPIException(
                f"Failed to connect to the CronMon API at {self.__SERVER_URL}"
            ) from e

        if not response.ok:
            message = response.json()["error"]["description"]
            if response.status_code == 401:
                raise InvalidAPIKey(message)
            raise CronMonAPIException(message)

        return response.json()["data"]
