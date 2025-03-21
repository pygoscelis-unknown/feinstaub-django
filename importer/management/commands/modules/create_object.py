#pylint: skip-file
import django
django.setup()
from importer.models import BME280, BMP180, BMP280, DHT22, DS18B20, HPM, HTU21D, PMS1003, PMS3003, PMS5003, PMS6003, PMS7003, PPD42NS, SDS011
def create(sensor_type, row):
    if sensor_type == "BME280":
        command = BME280.objects.create(
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
    if sensor_type == "BMP180":
        command = BMP180.objects.create(
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
    if sensor_type == "BMP280":
        command = BMP280.objects.create(
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
    if sensor_type == "DHT22":
        command = DHT22.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        temperature=row[6],
        humidity=row[7],
        )
    if sensor_type == "DS18B20":
        command = DS18B20.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        temperature=row[6],
        )
    if sensor_type == "HPM":
        command = HPM.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        P1=row[6],
        P2=row[7],
        )
    if sensor_type == "HTU21D":
        command = HTU21D.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        temperature=row[6],
        humidity=row[7],
        )
    if sensor_type == "PMS1003":
        command = PMS1003.objects.create(
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
    if sensor_type == "PMS3003":
        command = PMS3003.objects.create(
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
    if sensor_type == "PMS5003":
        command = PMS5003.objects.create(
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
    if sensor_type == "PMS6003":
        command = PMS6003.objects.create(
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
    if sensor_type == "PMS7003":
        command = PMS7003.objects.create(
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
    if sensor_type == "PPD42NS":
        command = PPD42NS.objects.create(
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
    if sensor_type == "SDS011":
        command = SDS011.objects.create(
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
