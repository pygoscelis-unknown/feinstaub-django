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

import multiprocessing

from django.apps import apps


class Command(BaseCommand):
    help = """
    Loads data from csv files into the database.
    This command downloads zip files of all sensor types available in zip format, unzip them and load data from the extracted csv files into the database.
    """

    def add_arguments(self, parser):
        parser.add_argument("--year", type=str, help="Format: YYYY")
        parser.add_argument("--month", type=str, help="Format: MM")
        parser.add_argument("--app", type=str, help="Your django app name")

    def handle(self, *args, **kwargs):

        base_url = get_sensor_archive_url()
        year = kwargs["year"]
        month = kwargs["month"]
        app = kwargs["app"]
        date = year + "-" + month

        # get all sensor types
        sensor_types = []
        for m in apps.get_app_config(app).get_models():
            sensor_types.append(m.__name__)

        start = time.time()

        for t in sensor_types:
            url = base_url + "/csv_per_month/" + date + "/" + date + "_" + t + ".zip"

            try:
                file_name = date + "_" + t
                print("Downloading zip ...", end="\r")
                urllib.request.urlretrieve(url, file_name + ".zip")
                with zipfile.ZipFile(file_name + ".zip", "r") as zip_ref:
                    print("Extracting zip ...")
                    zip_ref.extractall("./")

                with open(file_name + ".csv", newline="") as csvfile:
                    reader = csv.reader(csvfile, delimiter=";")
                    rows = [x for x in reader]
                    header = rows.pop(0)

                    create_objects(t, header, rows)

                # delete csv and zip
                for f in [file_name + ".zip", file_name + ".csv"]:
                    if os.path.exists(f):
                        print("Deleting file {} ...".format(f))
                        os.remove(f)
                        print("File {} deleted.".format(f))
                    else:
                        print("Failed to delete file {}.".format(f))

            except Exception as e:
                print(f"Error: {url}: {str(e)}")

        end = time.time()
        total_time = end - start
        print("time:", total_time)
