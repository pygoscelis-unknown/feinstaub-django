import datetime
import math


def main(header: list[str], row: list) -> list:
    """
    Converts illegal values from row into None.
    Returns row after conversion.
    """

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

    return row
