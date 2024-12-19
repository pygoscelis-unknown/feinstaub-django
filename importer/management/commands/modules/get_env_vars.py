"""
Gets values from env variables.
"""

import os
from dotenv import load_dotenv
from .validators import validate_url


def get_sensor_archive_url() -> str:
    """
    Gets sensor archive url from env file.
    """
    load_dotenv()
    url = os.environ.get("SENSOR_ARCHIVE_URL")

    @validate_url
    def main(url):
        return url
    return main(url)
