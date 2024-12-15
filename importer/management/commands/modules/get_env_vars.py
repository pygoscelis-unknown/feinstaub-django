import os
from dotenv import load_dotenv
from .validators import validateUrl


def get_sensor_archive_url() -> str:
    load_dotenv()
    url = os.environ.get("SENSOR_ARCHIVE_URL")

    @validateUrl
    def main(url):
        return url
    return main(url)
