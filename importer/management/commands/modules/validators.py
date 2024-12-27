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
        except ValueError:
            raise ValueError("Invalid data format, check the format is YYYY-MM-DD and the date is not out of range.")

    else:
        try:
            datetime.datetime.strptime(date, "%Y-%m")
        except ValueError:
            raise ValueError("Invalid data format, check the format is YYYY-MM and the date is not out of range.")


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
