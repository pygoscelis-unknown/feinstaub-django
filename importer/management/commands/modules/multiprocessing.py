"""
Create objects using multiprocessing.
"""

import multiprocessing
from itertools import repeat
from .convert_values import main as convert_values
from .create_object import create as create_object


def main(sensor_type, header, rows):
    """
    Create objects for sensor type with given data.
    When the system has access to 4 or more of the CPUs,
    this process uses the number of available CPUs - 2 CPUs,
    otherwise just 1 CPU.
    """
    cpu_amount = multiprocessing.cpu_count()
    if cpu_amount > 2:
        cpu_amount_to_use = cpu_amount - 2
    else:
        cpu_amount_to_use = 1

    if cpu_amount_to_use is not None:
        with multiprocessing.Pool(cpu_amount_to_use) as pool:
            pool.starmap(func, zip(repeat(sensor_type), repeat(header), rows))
    else:
        raise ValueError("Couln'd get your cpu amount.")


def func(sensor_type, header, row):
    """
    Create object for sensor type with given data.
    """
    new_row = convert_values(header, row)

    print(new_row, end="\r")
    print(end="\x1b[2K")
    create_object(sensor_type, new_row)
