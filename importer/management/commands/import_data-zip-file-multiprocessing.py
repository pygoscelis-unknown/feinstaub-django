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


class Command(BaseCommand):
    help = """
    Loads data from csv files into the database.
    This command downloads zip files of a specific sensor type available in zip format, unzip them and load data from the extracted csv files into the database.
    """

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str, help="Path to a local csv file")
        parser.add_argument(
            "--type",
            type=str,
            help="The name of the sensor type must additionaly be set",
        )

    def handle(self, *args, **kwargs):

        path = kwargs["path"]
        sensor_type = kwargs["type"]

        start = time.time()

        with open(path, newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            rows = [x for x in reader]
            header = rows.pop(0)

            create_objects(sensor_type, header, rows)

        end = time.time()
        total_time = end - start
        print("time:", total_time)
