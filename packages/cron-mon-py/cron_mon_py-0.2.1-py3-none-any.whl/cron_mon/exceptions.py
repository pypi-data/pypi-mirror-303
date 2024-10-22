"""Exceptions for the cron_mon package."""


class CronMonException(Exception):
    """Base exception for the cron_mon package."""


class CronMonAPIException(CronMonException):
    """Exception for API errors from the CronMon server."""


class InvalidAPIKey(CronMonAPIException):
    """Exception for an invalid API key."""
