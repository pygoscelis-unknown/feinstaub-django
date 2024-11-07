import os
from dotenv import load_dotenv

def get_sensor_archive_url():
    load_dotenv()
    return os.environ.get("SENSOR_ARCHIVE_URL")
