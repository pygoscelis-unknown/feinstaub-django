"""
Module: Sensor Type
"""


def get_sensor_type(a_href, date, is_zip=False) -> str:
    """
    Gets sensor type from html <a> tag
    Set is_zip True when using for zipfile via csv_per_month
    """
    tmp = a_href.split("_")
    sensor_type = None

    if len(tmp) > 1:
        date_index, sensor_index = None, None

        for i in range(len(tmp)):
            if tmp[i] == date:
                date_index = i

            if is_zip:
                if tmp[i] is not date:
                    sensor_index = i
            else:
                if tmp[i] == "sensor":
                    sensor_index = i

        if date_index is not None and sensor_index is not None:
            if is_zip:
                sensor_type = tmp[sensor_index].replace(".zip", "")
            else:
                if sensor_index - date_index == 2:
                    sensor_type = tmp[date_index + 1]

                else:
                    sensor_type = tmp[date_index + 1] + "_" + tmp[date_index + 2]

    if sensor_type is not None:
        return sensor_type

    raise ValueError("Cannot get sensor type.")
