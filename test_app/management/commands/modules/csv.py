import csv
import os
import urllib.request


def read_csv(url):
    response = urllib.request.urlopen(url)
    lines = [line.decode("utf-8") for line in response.readlines()]
    reader = csv.reader(lines, delimiter=";")

    return reader


def get_header(url):
    reader = read_csv(url)

    for row in reader:
        header = row
        break

    return header


def get_chunk(reader: str, chunksize: int):
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
            print("Deleting file {} ...".format(f), end="\r")
            os.remove(f)
            print(end="\x1b[2K")
            print("File {} deleted.".format(f))
        else:
            print("File {} does not exist, nothing to delete.".format(f))
