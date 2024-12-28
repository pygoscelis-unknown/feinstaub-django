import json
import datetime
from bs4 import BeautifulSoup
from django.core.management import BaseCommand
from .modules.csv import get_header
from .modules.sensor_type import get_sensor_type
from .modules.get_env_vars import get_sensor_archive_url
from .modules import requests
from .modules.validators import validate_date


def register(dictionary: dict, key: str, url: str, is_gz: bool):
    """
    Registers sensor type and prints register message
    """
    dictionary[key] = get_header(url, is_gz)
    print("Sensor type not in queue: Register sensor type", key, end="\r")


def skip(key: str):
    """
    Just prints skip message
    """
    print("Sensor type", key, "already in queue: Skip...", end="\r")


class Command(BaseCommand):
    help = """
    Gets header from a csv file.
    The date of the most recent csv file should be inserted as date arg to update header constantly.
    Check if the csv file of the date is already existing on archive before executing.
    """

    def add_arguments(self, parser):
        parser.add_argument(
            "--date",
            type=str,
            help="Date of the most recent csv file. Format: YYYY-MM-DD",
        )

    def handle(self, *args, **kwargs):
        website = get_sensor_archive_url()
        date = kwargs["date"]
        validate_date(date, True)

        current_year = datetime.datetime.now().year
        arg_year = datetime.datetime.fromisoformat(date).year
        year_path = ""
        is_gz = False

        if arg_year < current_year - 1:
            year_path = f"{arg_year}/"
            is_gz = True

        base_url = f"{website}/{year_path}{date}/"
        page = requests.get(base_url)

        print("Scanning page ...", end="\r")
        print(end="\x1b[2K")
        soup = BeautifulSoup(page.content, "html.parser")
        sensor_type_queue = {}

        for a in soup.find_all("a", href=True):
            try:
                sensor_type = get_sensor_type(a["href"], date)
            except ValueError:
                continue

            url = base_url + "/" + a["href"]

            if len(sensor_type_queue) == 0:
                register(sensor_type_queue, sensor_type, url, is_gz)
            else:
                if sensor_type not in sensor_type_queue:
                    register(sensor_type_queue, sensor_type, url, is_gz)
                else:
                    skip(sensor_type)

        print(end="\x1b[2K")
        print("Writing file ...")
        with open("sensor_csv_header.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(sensor_type_queue))
        print("See in root path: ./sensor_csv_header.json")
