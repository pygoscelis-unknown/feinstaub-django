from django.core.management import BaseCommand
from django.apps import apps
import sys
import csv
import os
from bs4 import BeautifulSoup
import urllib.request
import zipfile
import datetime
import time
import inquirer
from .modules.sensor_type import get_sensor_type
from .modules.multiprocessing import main as create_objects
from .modules.get_env_vars import get_sensor_archive_url
from .modules.csv import get_chunk, delete_sensor_data_files
from .modules.show_progress import show_download_progress


def import_monthly_data(date, sensor_type):
    base_url = get_sensor_archive_url()
    url = base_url + "/csv_per_month/" + date + "/" + date + "_" + sensor_type + ".zip"

    try:
        file_name = date + "_" + sensor_type
        print("Downloading zip ...")
        urllib.request.urlretrieve(url, file_name + ".zip", show_download_progress)
        with zipfile.ZipFile(file_name + ".zip", "r") as zip_ref:
            print("Extracting zip ...", end="\r")
            zip_ref.extractall("./")

        print("Opening file ...", end="\r")
        with open(file_name + ".csv", newline="") as csvfile:
            print("Reading file ...", end="\r")
            reader = csv.reader(csvfile, delimiter=";")

            print("Parsing content ...", end="\r")
            for index, chunk in get_chunk(reader, 100000):
                if index == 0:
                    header = chunk.pop(0)
                rows = [x for x in chunk]

                create_objects(sensor_type, header, rows)

        delete_sensor_data_files(file_name)

    except Exception as e:
        print(f"Error: {url}: {str(e)}")


class Command(BaseCommand):
    help = """
    Loads data from csv files into the database.
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

        if kwargs["year"] != None:
            year = kwargs["year"]
            if year not in years:
                raise ValueError("Invalid year or out of range")
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

        if kwargs["month"] != None:
            month = kwargs["month"]
            if month not in months:
                raise ValueError("Invalid month or out of range")
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

        if kwargs["all"]:
            import_all = True
        else:
            if kwargs["sensor"] != None:
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
                import_monthly_data(date, sensor_type)
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

            import_monthly_data(date, sensor_type)
            sys.exit(0)
