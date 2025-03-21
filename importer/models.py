#pylint: skip-file
from django.db import models
class BME280(models.Model):
    sensor_id = models.IntegerField(null=True, blank=True)
    sensor_type = models.CharField(max_length=255, blank=True)
    location = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    pressure = models.FloatField(null=True, blank=True)
    altitude = models.FloatField(null=True, blank=True)
    pressure_sealevel = models.FloatField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    class Meta:
        verbose_name = "BME280"
        verbose_name_plural = "BME280s"
class BMP180(models.Model):
    sensor_id = models.IntegerField(null=True, blank=True)
    sensor_type = models.CharField(max_length=255, blank=True)
    location = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    pressure = models.FloatField(null=True, blank=True)
    altitude = models.FloatField(null=True, blank=True)
    pressure_sealevel = models.FloatField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    class Meta:
        verbose_name = "BMP180"
        verbose_name_plural = "BMP180s"
class BMP280(models.Model):
    sensor_id = models.IntegerField(null=True, blank=True)
    sensor_type = models.CharField(max_length=255, blank=True)
    location = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    pressure = models.FloatField(null=True, blank=True)
    altitude = models.FloatField(null=True, blank=True)
    pressure_sealevel = models.FloatField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    class Meta:
        verbose_name = "BMP280"
        verbose_name_plural = "BMP280s"
class DHT22(models.Model):
    sensor_id = models.IntegerField(null=True, blank=True)
    sensor_type = models.CharField(max_length=255, blank=True)
    location = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    class Meta:
        verbose_name = "DHT22"
        verbose_name_plural = "DHT22s"
class DS18B20(models.Model):
    sensor_id = models.IntegerField(null=True, blank=True)
    sensor_type = models.CharField(max_length=255, blank=True)
    location = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    class Meta:
        verbose_name = "DS18B20"
        verbose_name_plural = "DS18B20s"
class HPM(models.Model):
    sensor_id = models.IntegerField(null=True, blank=True)
    sensor_type = models.CharField(max_length=255, blank=True)
    location = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    P1 = models.FloatField(null=True, blank=True)
    P2 = models.FloatField(null=True, blank=True)
    class Meta:
        verbose_name = "HPM"
        verbose_name_plural = "HPMs"
class HTU21D(models.Model):
    sensor_id = models.IntegerField(null=True, blank=True)
    sensor_type = models.CharField(max_length=255, blank=True)
    location = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    class Meta:
        verbose_name = "HTU21D"
        verbose_name_plural = "HTU21Ds"
class PMS1003(models.Model):
    sensor_id = models.IntegerField(null=True, blank=True)
    sensor_type = models.CharField(max_length=255, blank=True)
    location = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    P1 = models.FloatField(null=True, blank=True)
    P2 = models.FloatField(null=True, blank=True)
    P0 = models.FloatField(null=True, blank=True)
    class Meta:
        verbose_name = "PMS1003"
        verbose_name_plural = "PMS1003s"
class PMS3003(models.Model):
    sensor_id = models.IntegerField(null=True, blank=True)
    sensor_type = models.CharField(max_length=255, blank=True)
    location = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    P1 = models.FloatField(null=True, blank=True)
    P2 = models.FloatField(null=True, blank=True)
    P0 = models.FloatField(null=True, blank=True)
    class Meta:
        verbose_name = "PMS3003"
        verbose_name_plural = "PMS3003s"
class PMS5003(models.Model):
    sensor_id = models.IntegerField(null=True, blank=True)
    sensor_type = models.CharField(max_length=255, blank=True)
    location = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    P1 = models.FloatField(null=True, blank=True)
    P2 = models.FloatField(null=True, blank=True)
    P0 = models.FloatField(null=True, blank=True)
    class Meta:
        verbose_name = "PMS5003"
        verbose_name_plural = "PMS5003s"
class PMS6003(models.Model):
    sensor_id = models.IntegerField(null=True, blank=True)
    sensor_type = models.CharField(max_length=255, blank=True)
    location = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    P1 = models.FloatField(null=True, blank=True)
    P2 = models.FloatField(null=True, blank=True)
    P0 = models.FloatField(null=True, blank=True)
    class Meta:
        verbose_name = "PMS6003"
        verbose_name_plural = "PMS6003s"
class PMS7003(models.Model):
    sensor_id = models.IntegerField(null=True, blank=True)
    sensor_type = models.CharField(max_length=255, blank=True)
    location = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    P1 = models.FloatField(null=True, blank=True)
    P2 = models.FloatField(null=True, blank=True)
    P0 = models.FloatField(null=True, blank=True)
    class Meta:
        verbose_name = "PMS7003"
        verbose_name_plural = "PMS7003s"
class PPD42NS(models.Model):
    sensor_id = models.IntegerField(null=True, blank=True)
    sensor_type = models.CharField(max_length=255, blank=True)
    location = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    P1 = models.FloatField(null=True, blank=True)
    durP1 = models.FloatField(null=True, blank=True)
    ratioP1 = models.FloatField(null=True, blank=True)
    P2 = models.FloatField(null=True, blank=True)
    durP2 = models.FloatField(null=True, blank=True)
    ratioP2 = models.FloatField(null=True, blank=True)
    class Meta:
        verbose_name = "PPD42NS"
        verbose_name_plural = "PPD42NSs"
class SDS011(models.Model):
    sensor_id = models.IntegerField(null=True, blank=True)
    sensor_type = models.CharField(max_length=255, blank=True)
    location = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    P1 = models.FloatField(null=True, blank=True)
    durP1 = models.FloatField(null=True, blank=True)
    ratioP1 = models.FloatField(null=True, blank=True)
    P2 = models.FloatField(null=True, blank=True)
    durP2 = models.FloatField(null=True, blank=True)
    ratioP2 = models.FloatField(null=True, blank=True)
    class Meta:
        verbose_name = "SDS011"
        verbose_name_plural = "SDS011s"
