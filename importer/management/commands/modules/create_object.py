#pylint: skip-file
import django
django.setup()
from importer.models import bme280, bmp180, bmp280, dht22, ds18b20, hpm, htu21d, pms1003, pms3003, pms5003, pms6003, pms7003, ppd42ns, sds011
def create(sensor_type, row):
    if sensor_type == "bme280":
        command = bme280.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        pressure=row[6],
        altitude=row[7],
        pressure_sealevel=row[8],
        temperature=row[9],
        humidity=row[10],
        )
    if sensor_type == "bmp180":
        command = bmp180.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        pressure=row[6],
        altitude=row[7],
        pressure_sealevel=row[8],
        temperature=row[9],
        )
    if sensor_type == "bmp280":
        command = bmp280.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        pressure=row[6],
        altitude=row[7],
        pressure_sealevel=row[8],
        temperature=row[9],
        )
    if sensor_type == "dht22":
        command = dht22.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        temperature=row[6],
        humidity=row[7],
        )
    if sensor_type == "ds18b20":
        command = ds18b20.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        temperature=row[6],
        )
    if sensor_type == "hpm":
        command = hpm.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        P1=row[6],
        P2=row[7],
        )
    if sensor_type == "htu21d":
        command = htu21d.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        temperature=row[6],
        humidity=row[7],
        )
    if sensor_type == "pms1003":
        command = pms1003.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        P1=row[6],
        P2=row[7],
        P0=row[8],
        )
    if sensor_type == "pms3003":
        command = pms3003.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        P1=row[6],
        P2=row[7],
        P0=row[8],
        )
    if sensor_type == "pms5003":
        command = pms5003.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        P1=row[6],
        P2=row[7],
        P0=row[8],
        )
    if sensor_type == "pms6003":
        command = pms6003.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        P1=row[6],
        P2=row[7],
        P0=row[8],
        )
    if sensor_type == "pms7003":
        command = pms7003.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        P1=row[6],
        P2=row[7],
        P0=row[8],
        )
    if sensor_type == "ppd42ns":
        command = ppd42ns.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        P1=row[6],
        durP1=row[7],
        ratioP1=row[8],
        P2=row[9],
        durP2=row[10],
        ratioP2=row[11],
        )
    if sensor_type == "sds011":
        command = sds011.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        P1=row[6],
        durP1=row[7],
        ratioP1=row[8],
        P2=row[9],
        durP2=row[10],
        ratioP2=row[11],
        )
    return command
