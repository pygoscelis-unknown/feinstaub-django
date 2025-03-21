"""
Imports data from zip files available on:
    `http://archive.sensor.community/csv_per_month/`
Provides prompt to let user select year, month and sensor type.
These values can also be given as parameter.
Uses multiprocessing.
"""

import sys
import csv
import time
import datetime
import urllib.request
import zipfile
import inquirer
from django.core.management import BaseCommand
from django.apps import apps
from .modules.validators import validate_date
from .modules.multiprocessing import main as create_objects
from .modules.get_env_vars import get_sensor_archive_url
from .modules.csv import get_chunk, delete_sensor_data_files
from .modules.show_progress import show_download_progress


def import_monthly_data(date, sensor_type):
    """
    Import monthly data from given date and sensor type.
    """
    base_url = get_sensor_archive_url()
    url = base_url + "/csv_per_month/" + date + "/" + date + "_" + sensor_type.lower() + ".zip"

    file_name = date + "_" + sensor_type
    print("Downloading zip ...")
    urllib.request.urlretrieve(url, file_name + ".zip", show_download_progress)
    with zipfile.ZipFile(file_name + ".zip", "r") as zip_ref:
        print("Extracting zip ...", end="\r")
        zip_ref.extractall("./")

    print("Opening file ...", end="\r")
    with open(file_name + ".csv", newline="", encoding="utf-8") as csvfile:
        print("Reading file ...", end="\r")
        reader = csv.reader(csvfile, delimiter=";")

        print("Parsing content ...", end="\r")
        header = None
        for index, chunk in get_chunk(reader, 100000):
            if index == 0:
                header = chunk.pop(0)
            rows = list(chunk)

            if header:
                create_objects(sensor_type.lower(), header, rows)
            else:
                raise ValueError("Header is missing.")

    delete_sensor_data_files(file_name)


class Command(BaseCommand):
    """
    Downloads all zip files of the specified date and the specified sensor type (or all sensor types),
    unzips them,
    and loads data from those extracted csv files into database.
    """

    help = """
    Loads data from multiple zipped csv files into database.
    """

    def add_arguments(self, parser):
        group = parser.add_mutually_exclusive_group()

        parser.add_argument("--year", type=str, help="Format: YYYY")
        parser.add_argument("--month", type=str, help="Format: MM")
        group.add_argument(
            "--all", action="store_true", help="Import data of all sensor types"
        )
        group.add_argument(
            "--sensor",
            type=str,
            help="Sensor type whose data will be imported",
        )

    def handle(self, *args, **kwargs):
        sensor_types = []
        for m in apps.get_app_config("importer").get_models():
            sensor_types.append(m.__name__)
        years = []
        cur_year = datetime.datetime.now().year
        for i in range(2015, cur_year + 1):
            years.append(str(i))
        months = []
        for i in range(1, 13):
            months.append("%02d" % i)

        if kwargs["year"] is not None:
            year = kwargs["year"]
        else:
            qs = [
                inquirer.List(
                    "year",
                    message="Year of sensor data",
                    choices=years,
                    carousel=True,
                ),
            ]
            i = inquirer.prompt(qs)
            year = i["year"]

        if kwargs["month"] is not None:
            month = kwargs["month"]
        else:
            qs = [
                inquirer.List(
                    "month",
                    message="Month of sensor data",
                    choices=months,
                    carousel=True,
                ),
            ]
            i = inquirer.prompt(qs)
            month = i["month"]

        date = year + "-" + month
        validate_date(date)

        if kwargs["all"]:
            import_all = True
        else:
            if kwargs["sensor"] is not None:
                sensor_type = kwargs["sensor"]
                if sensor_type not in sensor_types:
                    raise ValueError("Invalid sensor name")

                import_monthly_data(date, sensor_type)
                sys.exit(0)

            else:
                ops = ["Yes", "No"]
                qs = [
                    inquirer.List(
                        "import_all",
                        message="Import data of all sensor types?",
                        choices=ops,
                        carousel=True,
                    ),
                ]
                i = inquirer.prompt(qs)
                if i["import_all"] == "Yes":
                    import_all = True
                else:
                    import_all = False

        if import_all:
            for sensor_type in sensor_types:
                try:
                    import_monthly_data(date, sensor_type)
                except Exception:
                    continue
            sys.exit(0)

        else:
            ops = sensor_types
            qs = [
                inquirer.List(
                    "sensor",
                    message="Select sensor type",
                    choices=ops,
                    carousel=True,
                ),
            ]
            i = inquirer.prompt(qs)
            sensor_type = i["sensor"]

            start = time.time()

            import_monthly_data(date, sensor_type)

            end = time.time()
            total_time = end - start
            print("Time:", total_time)
            sys.exit(0)
