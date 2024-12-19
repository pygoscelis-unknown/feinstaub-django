"""
CSV Handlers
"""

import csv
import os
import urllib.request
from typing import Iterator, Generator


def read_csv(url):
    """
    Read csv
    """
    with urllib.request.urlopen(url) as response:
        lines = [line.decode("utf-8") for line in response.readlines()]
    reader = csv.reader(lines, delimiter=";")

    return reader


def get_header(url):
    """
    Return first row as header
    """
    reader = read_csv(url)

    for row in reader:
        return row


def get_chunk(reader: Iterator[list[str]], chunksize: int) -> Generator[tuple[int, list[str]], None, None]:
    """
    Generates chunk to avoid OOM when a csv reader is too large to process at once
    """
    index = 0
    chunk = []
    for i, line in enumerate(reader):
        if i % chunksize == 0 and i > 0:
            yield index, chunk
            del chunk[:]
            index += 1
        chunk.append(line)
    yield index, chunk


def delete_sensor_data_files(file_name):
    """
    Delete csv/zip
    """
    for f in [file_name + ".zip", file_name + ".csv"]:
        if os.path.exists(f):
            print(f"Deleting file {f} ...", end="\r")
            os.remove(f)
            print(end="\x1b[2K")
            print(f"File {f} deleted.")
        else:
            print(f"File {f} does not exist, nothing to delete.")
