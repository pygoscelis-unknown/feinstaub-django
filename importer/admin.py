#pylint: skip-file
from django.contrib import admin
from .models import BME280, BMP180, BMP280, DHT22, DS18B20, HPM, HTU21D, PMS1003, PMS3003, PMS5003, PMS6003, PMS7003, PPD42NS, SDS011
admin.site.register(BME280)
admin.site.register(BMP180)
admin.site.register(BMP280)
admin.site.register(DHT22)
admin.site.register(DS18B20)
admin.site.register(HPM)
admin.site.register(HTU21D)
admin.site.register(PMS1003)
admin.site.register(PMS3003)
admin.site.register(PMS5003)
admin.site.register(PMS6003)
admin.site.register(PMS7003)
admin.site.register(PPD42NS)
admin.site.register(SDS011)
