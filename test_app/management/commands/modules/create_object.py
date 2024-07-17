from test_app.models import bme280, bmp180, bmp280, dht22, ds18b20, hpm, htu21d, laerm, nextpm, pms1003, pms3003, pms5003, pms6003, pms7003, ppd42ns, radiation_sbm19, radiation_sbm20, radiation_si22g, scd30, sds011, sht11, sht15, sht30, sht31, sht35, sht85, sps30
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
    if sensor_type == "laerm":
        command = laerm.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        noise_LAeq=row[6],
        noise_LA_min=row[7],
        noise_LA_max=row[8],
        noise_LA01=row[9],
        noise_LA95=row[10],
        )
    if sensor_type == "nextpm":
        command = nextpm.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        P1=row[6],
        P2=row[7],
        P0=row[8],
        N1=row[9],
        N25=row[10],
        N10=row[11],
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
    if sensor_type == "radiation_sbm19":
        command = radiation_sbm19.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        counts_per_minute=row[6],
        hv_pulses=row[7],
        tube=row[8],
        counts=row[9],
        sample_time_ms=row[10],
        )
    if sensor_type == "radiation_sbm20":
        command = radiation_sbm20.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        counts_per_minute=row[6],
        hv_pulses=row[7],
        tube=row[8],
        counts=row[9],
        sample_time_ms=row[10],
        )
    if sensor_type == "radiation_si22g":
        command = radiation_si22g.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        counts_per_minute=row[6],
        hv_pulses=row[7],
        tube=row[8],
        counts=row[9],
        sample_time_ms=row[10],
        )
    if sensor_type == "scd30":
        command = scd30.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        temperature=row[6],
        humidity=row[7],
        co2_ppm=row[8],
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
    if sensor_type == "sht11":
        command = sht11.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        temperature=row[6],
        humidity=row[7],
        )
    if sensor_type == "sht15":
        command = sht15.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        temperature=row[6],
        humidity=row[7],
        )
    if sensor_type == "sht30":
        command = sht30.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        temperature=row[6],
        humidity=row[7],
        )
    if sensor_type == "sht31":
        command = sht31.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        temperature=row[6],
        humidity=row[7],
        )
    if sensor_type == "sht35":
        command = sht35.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        temperature=row[6],
        humidity=row[7],
        )
    if sensor_type == "sht85":
        command = sht85.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        temperature=row[6],
        humidity=row[7],
        )
    if sensor_type == "sps30":
        command = sps30.objects.create(
        sensor_id=row[0],
        sensor_type=row[1],
        location=row[2],
        lat=row[3],
        lon=row[4],
        timestamp=row[5],
        P1=row[6],
        P4=row[7],
        P2=row[8],
        P0=row[9],
        N10=row[10],
        N4=row[11],
        N25=row[12],
        N1=row[13],
        N05=row[14],
        TS=row[15],
        )
    return command
