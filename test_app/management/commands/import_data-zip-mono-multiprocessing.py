from django.core.management import BaseCommand
import csv
import os

from bs4 import BeautifulSoup
import urllib.request
import zipfile
import datetime
import time
from .modules.sensor_type import get_sensor_type
from .modules.multiprocessing import main as create_objects
from .modules.get_env_vars import get_sensor_archive_url


class Command(BaseCommand):
    help = """
    Loads data from csv files into the database.
    This command downloads zip files of a specific sensor type available in zip format, unzip them and load data from the extracted csv files into the database.
    """

    def add_arguments(self, parser):
        parser.add_argument("--year", type=str, help="Format: YYYY")
        parser.add_argument("--month", type=str, help="Format: MM")
        parser.add_argument("--type", type=str, help="The name of the target sensor type")

    def handle(self, *args, **kwargs):

        base_url = get_sensor_archive_url()
        year = kwargs["year"]
        month = kwargs["month"]
        date = year + "-" + month
        sensor_type = kwargs["type"]
        url = (
            base_url
            + "/csv_per_month/"
            + date
            + "/"
            + date
            + "_"
            + sensor_type
            + ".zip"
        )
        file_name = date + "_" + sensor_type

        start = time.time()

        print("Downloading zip ...", end="\r")
        urllib.request.urlretrieve(url, file_name + ".zip")
        with zipfile.ZipFile(file_name + ".zip", "r") as zip_ref:
            print("Extracting zip ...")
            zip_ref.extractall("./")

        with open(file_name + ".csv", newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            rows = [x for x in reader]
            header = rows.pop(0)

            create_objects(sensor_type, header, rows)

        # delete csv and zip
        for f in [file_name + ".zip", file_name + ".csv"]:
            if os.path.exists(f):
                print("Deleting file {} ...".format(f))
                os.remove(f)
                print("File {} deleted.".format(f))
            else:
                print("Failed to delete file {}.".format(f))

        end = time.time()
        total_time = end - start
        print("time:", total_time)
