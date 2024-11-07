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
from .modules.csv import get_chunk, delete_sensor_data_files


class Command(BaseCommand):
    help = """
    Loads data from csv files into the database.
    This command downloads zip files of a specific sensor type available in zip format, unzip them and load data from the extracted csv files into the database.
    """

    def add_arguments(self, parser):
        parser.add_argument("--year", type=str, help="Format: YYYY")
        parser.add_argument("--month", type=str, help="Format: MM")
        parser.add_argument(
            "--type", type=str, help="The name of the target sensor type"
        )

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

        end = time.time()
        total_time = end - start
        print("time:", total_time)
