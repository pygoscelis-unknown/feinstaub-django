import csv
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
