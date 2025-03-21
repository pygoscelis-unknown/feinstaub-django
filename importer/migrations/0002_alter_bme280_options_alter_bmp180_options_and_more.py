# Generated by Django 5.1.7 on 2025-03-21 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("importer", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bme280",
            options={"verbose_name": "BME280", "verbose_name_plural": "BME280s"},
        ),
        migrations.AlterModelOptions(
            name="bmp180",
            options={"verbose_name": "BMP180", "verbose_name_plural": "BMP180s"},
        ),
        migrations.AlterModelOptions(
            name="bmp280",
            options={"verbose_name": "BMP280", "verbose_name_plural": "BMP280s"},
        ),
        migrations.AlterModelOptions(
            name="dht22",
            options={"verbose_name": "DHT22", "verbose_name_plural": "DHT22s"},
        ),
        migrations.AlterModelOptions(
            name="ds18b20",
            options={"verbose_name": "DS18B20", "verbose_name_plural": "DS18B20s"},
        ),
        migrations.AlterModelOptions(
            name="hpm",
            options={"verbose_name": "HPM", "verbose_name_plural": "HPMs"},
        ),
        migrations.AlterModelOptions(
            name="htu21d",
            options={"verbose_name": "HTU21D", "verbose_name_plural": "HTU21Ds"},
        ),
        migrations.AlterModelOptions(
            name="pms1003",
            options={"verbose_name": "PMS1003", "verbose_name_plural": "PMS1003s"},
        ),
        migrations.AlterModelOptions(
            name="pms3003",
            options={"verbose_name": "PMS3003", "verbose_name_plural": "PMS3003s"},
        ),
        migrations.AlterModelOptions(
            name="pms5003",
            options={"verbose_name": "PMS5003", "verbose_name_plural": "PMS5003s"},
        ),
        migrations.AlterModelOptions(
            name="pms6003",
            options={"verbose_name": "PMS6003", "verbose_name_plural": "PMS6003s"},
        ),
        migrations.AlterModelOptions(
            name="pms7003",
            options={"verbose_name": "PMS7003", "verbose_name_plural": "PMS7003s"},
        ),
        migrations.AlterModelOptions(
            name="ppd42ns",
            options={"verbose_name": "PPD42NS", "verbose_name_plural": "PPD42NSs"},
        ),
        migrations.AlterModelOptions(
            name="sds011",
            options={"verbose_name": "SDS011", "verbose_name_plural": "SDS011s"},
        ),
    ]
