#pylint: skip-file
from django.contrib import admin
from .models import bme280, bmp180, bmp280, dht22, ds18b20, hpm, htu21d, pms1003, pms3003, pms5003, pms6003, pms7003, ppd42ns, sds011
admin.site.register(bme280)
admin.site.register(bmp180)
admin.site.register(bmp280)
admin.site.register(dht22)
admin.site.register(ds18b20)
admin.site.register(hpm)
admin.site.register(htu21d)
admin.site.register(pms1003)
admin.site.register(pms3003)
admin.site.register(pms5003)
admin.site.register(pms6003)
admin.site.register(pms7003)
admin.site.register(ppd42ns)
admin.site.register(sds011)
