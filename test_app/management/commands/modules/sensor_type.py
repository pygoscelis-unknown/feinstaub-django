def get_sensor_type(a_href, date):
    '''
    get sensor type from a tag
    '''
    tmp = a_href.split("_")
    sensor_type = None

    if (len(tmp) > 1):
        date_index, sensor_index = None, None

        for i in range(len(tmp)):
            if tmp[i] == date:
                date_index = i

            if tmp[i] == "sensor":
                sensor_index = i

        if date_index != None and sensor_index != None:
            if sensor_index - date_index == 2:
                sensor_type = tmp[date_index + 1]

            else:
                sensor_type = tmp[date_index + 1] + "_" + tmp[date_index + 2]

    return sensor_type
