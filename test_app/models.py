from django.db import models
from django.conf import settings
import os

class BaseModel(models.Model):
    objects = models.Manager()
    class Meta:
        abstract = True


class bme280(BaseModel):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    pressure = models.FloatField(null=True)
#
    altitude = models.FloatField(null=True)
#
    pressure_sealevel = models.FloatField(null=True)
#
    temperature = models.FloatField(null=True)
#
    humidity = models.FloatField(null=True)
class bmp180(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    pressure = models.FloatField(null=True)
#
    altitude = models.FloatField(null=True)
#
    pressure_sealevel = models.FloatField(null=True)
#
    temperature = models.FloatField(null=True)
class bmp280(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    pressure = models.FloatField(null=True)
#
    altitude = models.FloatField(null=True)
#
    pressure_sealevel = models.FloatField(null=True)
#
    temperature = models.FloatField(null=True)
class dht22(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    temperature = models.FloatField(null=True)
#
    humidity = models.FloatField(null=True)
class ds18b20(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    temperature = models.FloatField(null=True)
class hpm(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    P1 = models.FloatField(null=True)
#
    P2 = models.FloatField(null=True)
class htu21d(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    temperature = models.FloatField(null=True)
#
    humidity = models.FloatField(null=True)
class laerm(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    noise_LAeq = models.FloatField(null=True)
#
    noise_LA_min = models.FloatField(null=True)
#
    noise_LA_max = models.FloatField(null=True)
#
    noise_LA01 = models.FloatField(null=True)
#
    noise_LA95 = models.FloatField(null=True)
class nextpm(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    P1 = models.FloatField(null=True)
#
    P2 = models.FloatField(null=True)
#
    P0 = models.FloatField(null=True)
#
    N1 = models.FloatField(null=True)
#
    N25 = models.FloatField(null=True)
#
    N10 = models.FloatField(null=True)
class pms1003(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    P1 = models.FloatField(null=True)
#
    P2 = models.FloatField(null=True)
#
    P0 = models.FloatField(null=True)
class pms3003(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    P1 = models.FloatField(null=True)
#
    P2 = models.FloatField(null=True)
#
    P0 = models.FloatField(null=True)
class pms5003(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    P1 = models.FloatField(null=True)
#
    P2 = models.FloatField(null=True)
#
    P0 = models.FloatField(null=True)
class pms6003(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    P1 = models.FloatField(null=True)
#
    P2 = models.FloatField(null=True)
#
    P0 = models.FloatField(null=True)
class pms7003(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    P1 = models.FloatField(null=True)
#
    P2 = models.FloatField(null=True)
#
    P0 = models.FloatField(null=True)
class ppd42ns(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    P1 = models.FloatField(null=True)
#
    durP1 = models.FloatField(null=True)
#
    ratioP1 = models.FloatField(null=True)
#
    P2 = models.FloatField(null=True)
#
    durP2 = models.FloatField(null=True)
#
    ratioP2 = models.FloatField(null=True)
class radiation_sbm19(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    counts_per_minute = models.FloatField(null=True)
#
    hv_pulses = models.FloatField(null=True)
#
    tube = models.FloatField(null=True)
#
    counts = models.FloatField(null=True)
#
    sample_time_ms = models.FloatField(null=True)
class radiation_sbm20(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    counts_per_minute = models.FloatField(null=True)
#
    hv_pulses = models.FloatField(null=True)
#
    tube = models.FloatField(null=True)
#
    counts = models.FloatField(null=True)
#
    sample_time_ms = models.FloatField(null=True)
class radiation_si22g(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    counts_per_minute = models.FloatField(null=True)
#
    hv_pulses = models.FloatField(null=True)
#
    tube = models.FloatField(null=True)
#
    counts = models.FloatField(null=True)
#
    sample_time_ms = models.FloatField(null=True)
class scd30(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    temperature = models.FloatField(null=True)
#
    humidity = models.FloatField(null=True)
#
    co2_ppm = models.FloatField(null=True)
class sds011(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    P1 = models.FloatField(null=True)
#
    durP1 = models.FloatField(null=True)
#
    ratioP1 = models.FloatField(null=True)
#
    P2 = models.FloatField(null=True)
#
    durP2 = models.FloatField(null=True)
#
    ratioP2 = models.FloatField(null=True)
class sht11(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    temperature = models.FloatField(null=True)
#
    humidity = models.FloatField(null=True)
class sht15(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    temperature = models.FloatField(null=True)
#
    humidity = models.FloatField(null=True)
class sht30(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    temperature = models.FloatField(null=True)
#
    humidity = models.FloatField(null=True)
class sht31(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    temperature = models.FloatField(null=True)
#
    humidity = models.FloatField(null=True)
class sht35(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    temperature = models.FloatField(null=True)
#
    humidity = models.FloatField(null=True)
class sht85(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    temperature = models.FloatField(null=True)
#
    humidity = models.FloatField(null=True)
class sps30(models.Model):
#
    sensor_id = models.IntegerField(null=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True)
#
    lat = models.FloatField(null=True)
#
    lon = models.FloatField(null=True)
#
    timestamp = models.DateTimeField(null=True)
#
    P1 = models.FloatField(null=True)
#
    P4 = models.FloatField(null=True)
#
    P2 = models.FloatField(null=True)
#
    P0 = models.FloatField(null=True)
#
    N10 = models.FloatField(null=True)
#
    N4 = models.FloatField(null=True)
#
    N25 = models.FloatField(null=True)
#
    N1 = models.FloatField(null=True)
#
    N05 = models.FloatField(null=True)
#
    TS = models.FloatField(null=True)
