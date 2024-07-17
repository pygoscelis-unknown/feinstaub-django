from django.urls import path, include
from rest_framework import routers
from .views import Bme280ViewSet, Bmp180ViewSet, Bmp280ViewSet, Dht22ViewSet, Ds18b20ViewSet, HpmViewSet, Htu21dViewSet, LaermViewSet, NextpmViewSet, Pms1003ViewSet, Pms3003ViewSet, Pms5003ViewSet, Pms6003ViewSet, Pms7003ViewSet, Ppd42nsViewSet, Radiation_sbm19ViewSet, Radiation_sbm20ViewSet, Radiation_si22gViewSet, Scd30ViewSet, Sds011ViewSet, Sht11ViewSet, Sht15ViewSet, Sht30ViewSet, Sht31ViewSet, Sht35ViewSet, Sht85ViewSet, Sps30ViewSet
router = routers.DefaultRouter()
router.register(r'bme280', Bme280ViewSet)
router.register(r'bmp180', Bmp180ViewSet)
router.register(r'bmp280', Bmp280ViewSet)
router.register(r'dht22', Dht22ViewSet)
router.register(r'ds18b20', Ds18b20ViewSet)
router.register(r'hpm', HpmViewSet)
router.register(r'htu21d', Htu21dViewSet)
router.register(r'laerm', LaermViewSet)
router.register(r'nextpm', NextpmViewSet)
router.register(r'pms1003', Pms1003ViewSet)
router.register(r'pms3003', Pms3003ViewSet)
router.register(r'pms5003', Pms5003ViewSet)
router.register(r'pms6003', Pms6003ViewSet)
router.register(r'pms7003', Pms7003ViewSet)
router.register(r'ppd42ns', Ppd42nsViewSet)
router.register(r'radiation_sbm19', Radiation_sbm19ViewSet)
router.register(r'radiation_sbm20', Radiation_sbm20ViewSet)
router.register(r'radiation_si22g', Radiation_si22gViewSet)
router.register(r'scd30', Scd30ViewSet)
router.register(r'sds011', Sds011ViewSet)
router.register(r'sht11', Sht11ViewSet)
router.register(r'sht15', Sht15ViewSet)
router.register(r'sht30', Sht30ViewSet)
router.register(r'sht31', Sht31ViewSet)
router.register(r'sht35', Sht35ViewSet)
router.register(r'sht85', Sht85ViewSet)
router.register(r'sps30', Sps30ViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
