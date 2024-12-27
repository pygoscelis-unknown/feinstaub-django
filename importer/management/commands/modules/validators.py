"""
Validators
"""

import datetime
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validate_date(date: str, with_day=False):
    """
    Validates date format
    """

    if with_day:
        try:
            datetime.date.fromisoformat(date)
        except ValueError as e:
            raise ValueError("Invalid data format, check the format is YYYY-MM-DD and the date is not out of range.") from e

    else:
        try:
            datetime.datetime.strptime(date, "%Y-%m")
        except ValueError as e:
            raise ValueError("Invalid data format, check the format is YYYY-MM and the date is not out of range.") from e


def validate_url(func):
    """
    Decorator for validating url.
    """

    def inner(url):
        val = URLValidator()
        try:
            val(url)
        except ValidationError as e:
            raise ValidationError(e) from e

        return func(url)

    return inner
