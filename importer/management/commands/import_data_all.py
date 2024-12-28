import time
import datetime
from bs4 import BeautifulSoup
from django.core.management import BaseCommand
from .modules.sensor_type import get_sensor_type
from .modules.create_object import create
from .modules.get_env_vars import get_sensor_archive_url
from .modules.csv import read_csv
from .modules.convert_values import main as convert_values
from .modules import requests
from .modules.validators import validate_date


class Command(BaseCommand):
    """
    Loads data from all csv files of the date into database.
    The date must be set in the following format: YYYY-MM-DD
    Doesn't use multiprocessing.
    """

    help = """
    Loads data from all csv files of the date into database.
    """

    def add_arguments(self, parser):
        parser.add_argument("--date", type=str, help="Format: YYYY-MM-DD")

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

        base_url = f"{website}/{year_path}{date}"
        page = requests.get(base_url)
        soup = BeautifulSoup(page.content, "html.parser")

        start = time.time()
        object_count = 0
        for i in soup.find_all("a", href=True):
            if date in i["href"]:
                sensor_type = get_sensor_type(i["href"], date)
                sensor_type = sensor_type.replace("-", "")

                url = f"{base_url}/{i['href']}"

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
                        print(str(object_count) + ". object created.")
        print("total:", object_count, "objects")

        end = time.time()
        total_time = end - start
        print("time:", total_time)
