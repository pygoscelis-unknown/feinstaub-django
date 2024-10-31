from django.core.management import BaseCommand
import csv
import os

from bs4 import BeautifulSoup
import urllib.request
import zipfile
import datetime
import time
import math
from .modules.sensor_type import get_sensor_type
from .modules.create_object import create
from .modules.get_env_vars import get_sensor_archive_url


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
        object_count = 0

        print("Downloading zip ...")
        urllib.request.urlretrieve(url, file_name + ".zip")
        with zipfile.ZipFile(file_name + ".zip", "r") as zip_ref:
            print("Extracting zip ...", end="\r")
            zip_ref.extractall("./")

        with open(file_name + ".csv", newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=";")

            index = 0
            header = []

            for row in reader:
                # ignore first header row
                if index == 0:
                    for i in range(len(row)):
                        header.append(row[i])
                    index += 1

                else:
                    # convert illegal values
                    for i in range(len(row)):
                        if header[i] != "sensor_type":
                            if header[i] == "sensor_id" or header[i] == "location":
                                # int
                                try:
                                    row[i] = int(row[i])
                                except ValueError:
                                    row[i] = None

                            elif header[i] == "timestamp":
                                # timestamp
                                try:
                                    row[i] = datetime.datetime.fromisoformat(row[i])
                                except ValueError:
                                    row[i] = None

                            else:
                                # float
                                try:
                                    row[i] = float(row[i])
                                    if math.isnan(row[i]):
                                        row[i] = None
                                except ValueError:
                                    row[i] = None

                    create(sensor_type, row)

                    object_count += 1
                    print(str(object_count) + ". object created.", end="\r")

        # delete csv and zip
        for f in [file_name + ".zip", file_name + ".csv"]:
            if os.path.exists(f):
                print("Deleting file {} ...".format(f))
                os.remove(f)
                print("File {} deleted.".format(f))
            else:
                print("Failed to delete file {}.".format(f))
        print("total:", object_count, "objects", end="\r")

        end = time.time()
        total_time = end - start
        print("time:", total_time)
