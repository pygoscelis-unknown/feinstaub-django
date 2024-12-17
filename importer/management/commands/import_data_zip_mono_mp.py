"""
Imports data from a particular zip file available on:
    `http://archive.sensor.community/csv_per_month/`
Uses multiprocessing.
"""

import csv
import urllib.request
import zipfile
import time
from django.core.management import BaseCommand
from .modules.multiprocessing import main as create_objects
from .modules.get_env_vars import get_sensor_archive_url
from .modules.csv import get_chunk, delete_sensor_data_files
from .modules.show_progress import show_download_progress


class Command(BaseCommand):
    """
    Downloads a zip file of the specified sensor type, unzips them,
    and loads data from the extracted csv file into database.
    """

    help = """
    Loads data from a zipped csv file into database.
    """

    def add_arguments(self, parser):
        parser.add_argument("--year", type=str, help="Format: YYYY")
        parser.add_argument("--month", type=str, help="Format: MM")
        parser.add_argument(
            "--type", type=str, help="The name of the target sensor type"
        )

    def handle(self, *args, **kwargs):

        base_url = get_sensor_archive_url()
        date = kwargs["year"] + "-" + kwargs["month"]
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
                    create_objects(sensor_type, header, rows)
                else:
                    raise ValueError("Header is missing.")

        delete_sensor_data_files(file_name)

        end = time.time()
        total_time = end - start
        print("time:", total_time)
