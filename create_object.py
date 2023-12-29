from test_app.models import bme280
from test_app.models import bmp180
from test_app.models import bmp280
from test_app.models import dht22
from test_app.models import ds18b20
from test_app.models import hpm
from test_app.models import htu21d
from test_app.models import laerm
from test_app.models import nextpm
from test_app.models import pms1003
from test_app.models import pms3003
from test_app.models import pms5003
from test_app.models import pms6003
from test_app.models import pms7003
from test_app.models import ppd42ns
from test_app.models import radiation_sbm19
from test_app.models import radiation_sbm20
from test_app.models import radiation_si22g
from test_app.models import scd30
from test_app.models import sds011
from test_app.models import sht11
from test_app.models import sht15
from test_app.models import sht30
from test_app.models import sht31
from test_app.models import sht35
from test_app.models import sht85
from test_app.models import sps30
def create(sensor_type, row):
#
    if sensor_type == "bme280":
        command = bme280.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        pressure=float(row[6]),
#
        altitude=float(row[7]),
#
        pressure_sealevel=float(row[8]),
#
        temperature=float(row[9]),
#
        humidity=float(row[10]),
#
        )
#
    if sensor_type == "bmp180":
        command = bmp180.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        pressure=float(row[6]),
#
        altitude=float(row[7]),
#
        pressure_sealevel=float(row[8]),
#
        temperature=float(row[9]),
#
        )
#
    if sensor_type == "bmp280":
        command = bmp280.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        pressure=float(row[6]),
#
        altitude=float(row[7]),
#
        pressure_sealevel=float(row[8]),
#
        temperature=float(row[9]),
#
        )
#
    if sensor_type == "dht22":
        command = dht22.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        temperature=float(row[6]),
#
        humidity=float(row[7]),
#
        )
#
    if sensor_type == "ds18b20":
        command = ds18b20.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        temperature=float(row[6]),
#
        )
#
    if sensor_type == "hpm":
        command = hpm.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        P1=float(row[6]),
#
        P2=float(row[7]),
#
        )
#
    if sensor_type == "htu21d":
        command = htu21d.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        temperature=float(row[6]),
#
        humidity=float(row[7]),
#
        )
#
    if sensor_type == "laerm":
        command = laerm.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        noise_LAeq=float(row[6]),
#
        noise_LA_min=float(row[7]),
#
        noise_LA_max=float(row[8]),
#
        noise_LA01=float(row[9]),
#
        noise_LA95=float(row[10]),
#
        )
#
    if sensor_type == "nextpm":
        command = nextpm.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        P1=float(row[6]),
#
        P2=float(row[7]),
#
        P0=float(row[8]),
#
        N1=float(row[9]),
#
        N25=float(row[10]),
#
        N10=float(row[11]),
#
        )
#
    if sensor_type == "pms1003":
        command = pms1003.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        P1=float(row[6]),
#
        P2=float(row[7]),
#
        P0=float(row[8]),
#
        )
#
    if sensor_type == "pms3003":
        command = pms3003.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        P1=float(row[6]),
#
        P2=float(row[7]),
#
        P0=float(row[8]),
#
        )
#
    if sensor_type == "pms5003":
        command = pms5003.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        P1=float(row[6]),
#
        P2=float(row[7]),
#
        P0=float(row[8]),
#
        )
#
    if sensor_type == "pms6003":
        command = pms6003.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        P1=float(row[6]),
#
        P2=float(row[7]),
#
        P0=float(row[8]),
#
        )
#
    if sensor_type == "pms7003":
        command = pms7003.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        P1=float(row[6]),
#
        P2=float(row[7]),
#
        P0=float(row[8]),
#
        )
#
    if sensor_type == "ppd42ns":
        command = ppd42ns.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        P1=float(row[6]),
#
        durP1=float(row[7]),
#
        ratioP1=float(row[8]),
#
        P2=float(row[9]),
#
        durP2=float(row[10]),
#
        ratioP2=float(row[11]),
#
        )
#
    if sensor_type == "radiation_sbm19":
        command = radiation_sbm19.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        counts_per_minute=float(row[6]),
#
        hv_pulses=float(row[7]),
#
        tube=float(row[8]),
#
        counts=float(row[9]),
#
        sample_time_ms=float(row[10]),
#
        )
#
    if sensor_type == "radiation_sbm20":
        command = radiation_sbm20.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        counts_per_minute=float(row[6]),
#
        hv_pulses=float(row[7]),
#
        tube=float(row[8]),
#
        counts=float(row[9]),
#
        sample_time_ms=float(row[10]),
#
        )
#
    if sensor_type == "radiation_si22g":
        command = radiation_si22g.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        counts_per_minute=float(row[6]),
#
        hv_pulses=float(row[7]),
#
        tube=float(row[8]),
#
        counts=float(row[9]),
#
        sample_time_ms=float(row[10]),
#
        )
#
    if sensor_type == "scd30":
        command = scd30.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        temperature=float(row[6]),
#
        humidity=float(row[7]),
#
        co2_ppm=float(row[8]),
#
        )
#
    if sensor_type == "sds011":
        command = sds011.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        P1=float(row[6]),
#
        durP1=float(row[7]),
#
        ratioP1=float(row[8]),
#
        P2=float(row[9]),
#
        durP2=float(row[10]),
#
        ratioP2=float(row[11]),
#
        )
#
    if sensor_type == "sht11":
        command = sht11.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        temperature=float(row[6]),
#
        humidity=float(row[7]),
#
        )
#
    if sensor_type == "sht15":
        command = sht15.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        temperature=float(row[6]),
#
        humidity=float(row[7]),
#
        )
#
    if sensor_type == "sht30":
        command = sht30.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        temperature=float(row[6]),
#
        humidity=float(row[7]),
#
        )
#
    if sensor_type == "sht31":
        command = sht31.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        temperature=float(row[6]),
#
        humidity=float(row[7]),
#
        )
#
    if sensor_type == "sht35":
        command = sht35.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        temperature=float(row[6]),
#
        humidity=float(row[7]),
#
        )
#
    if sensor_type == "sht85":
        command = sht85.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        temperature=float(row[6]),
#
        humidity=float(row[7]),
#
        )
#
    if sensor_type == "sps30":
        command = sps30.objects.create(
#
        sensor_id=int(row[0]),
#
        sensor_type=row[1],
#
        location=int(row[2]),
#
        lat=float(row[3]),
#
        lon=float(row[4]),
#
        timestamp=row[5],
#
        P1=float(row[6]),
#
        P4=float(row[7]),
#
        P2=float(row[8]),
#
        P0=float(row[9]),
#
        N10=float(row[10]),
#
        N4=float(row[11]),
#
        N25=float(row[12]),
#
        N1=float(row[13]),
#
        N05=float(row[14]),
#
        TS=float(row[15]),
#
        )
#
    return command
