import django

django.setup()
from itertools import repeat
from .create_object import create as create_object
import datetime

import multiprocessing


def main(sensor_type, header, rows):
    cpu_amount = multiprocessing.cpu_count()
    if cpu_amount > 2:
        cpu_amount_to_use = cpu_amount - 2
    else:
        cpu_amount_to_use = 1

    if cpu_amount_to_use != None:
        with multiprocessing.Pool(cpu_amount_to_use) as pool:
            pool.starmap(func, zip(repeat(sensor_type), repeat(header), rows))
    else:
        raise ValueError("Couln'd get your cpu amount.")


def func(sensor_type, header, row):
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
                except ValueError:
                    row[i] = None

    print(row)
    create_object(sensor_type, row)
    print("creating object ...", end="\r")
