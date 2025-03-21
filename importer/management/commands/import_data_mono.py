import time
import datetime
from bs4 import BeautifulSoup
from django.core.management import BaseCommand
from .modules.csv import read_csv
from .modules.sensor_type import get_sensor_type
from .modules.create_object import create
from .modules.get_env_vars import get_sensor_archive_url
from .modules.convert_values import main as convert_values
from .modules import requests
from .modules.validators import validate_date


class Command(BaseCommand):
    """
    Loads data from csv files of a specific sensor type into database.
    The date must be set in the following format: YYYY-MM-DD
    """

    help = """
    Loads data from csv files of a specific sensor type into database.
    """

    def add_arguments(self, parser):
        parser.add_argument("--date", type=str, help="Format: YYYY-MM-DD")
        parser.add_argument(
            "--type", type=str, help="The name of the target sensor type"
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

        inserted_sensor_type = kwargs["type"]
        base_url = f"{website}/{year_path}{date}"
        page = requests.get(base_url)
        soup = BeautifulSoup(page.content, "html.parser")

        start = time.time()
        object_count = 0
        for i in soup.find_all("a", href=True):
            if date in i["href"]:
                try:
                    sensor_type = get_sensor_type(i["href"], date)
                except ValueError:
                    continue

                sensor_type = sensor_type.replace("-", "")
                if sensor_type is not None and inserted_sensor_type.lower() == sensor_type:
                    url = f"{base_url}/{i['href']}"
                    print("Importing from:", url)

                    reader = read_csv(url, is_gz)

                    index = 0
                    header = []

                    for row in reader:
                        # ignore first header row
                        if index == 0:
                            for i in range(len(row)):
                                header.append(row[i])
                            index += 1

                        else:
                            new_row = convert_values(header, row)
                            create(sensor_type, new_row)

                            object_count += 1
                    print("Done.")
        print("Total:", object_count, "objects")

        end = time.time()
        total_time = end - start
        print("Time:", total_time)
