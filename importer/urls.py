#pylint: skip-file
from django.urls import path, include
from rest_framework import routers
from .views import Bme280ViewSet, Bmp180ViewSet, Bmp280ViewSet, Dht22ViewSet, Ds18b20ViewSet, HpmViewSet, Htu21dViewSet, LaermViewSet, Pms1003ViewSet, Pms3003ViewSet, Pms5003ViewSet, Pms6003ViewSet, Pms7003ViewSet, Ppd42nsViewSet, Radiation_sbm19ViewSet, Radiation_sbm20ViewSet, Radiation_si22gViewSet, Scd30ViewSet, Sds011ViewSet, Sen5xViewSet, Sht10ViewSet, Sht11ViewSet, Sht15ViewSet, Sht30ViewSet, Sht31ViewSet, Sht35ViewSet, Sps30ViewSet
router = routers.DefaultRouter()
router.register(r'bme280', Bme280ViewSet, basename='bme280')
router.register(r'bmp180', Bmp180ViewSet, basename='bmp180')
router.register(r'bmp280', Bmp280ViewSet, basename='bmp280')
router.register(r'dht22', Dht22ViewSet, basename='dht22')
router.register(r'ds18b20', Ds18b20ViewSet, basename='ds18b20')
router.register(r'hpm', HpmViewSet, basename='hpm')
router.register(r'htu21d', Htu21dViewSet, basename='htu21d')
router.register(r'laerm', LaermViewSet, basename='laerm')
router.register(r'pms1003', Pms1003ViewSet, basename='pms1003')
router.register(r'pms3003', Pms3003ViewSet, basename='pms3003')
router.register(r'pms5003', Pms5003ViewSet, basename='pms5003')
router.register(r'pms6003', Pms6003ViewSet, basename='pms6003')
router.register(r'pms7003', Pms7003ViewSet, basename='pms7003')
router.register(r'ppd42ns', Ppd42nsViewSet, basename='ppd42ns')
router.register(r'radiation_sbm19', Radiation_sbm19ViewSet, basename='radiation_sbm19')
router.register(r'radiation_sbm20', Radiation_sbm20ViewSet, basename='radiation_sbm20')
router.register(r'radiation_si22g', Radiation_si22gViewSet, basename='radiation_si22g')
router.register(r'scd30', Scd30ViewSet, basename='scd30')
router.register(r'sds011', Sds011ViewSet, basename='sds011')
router.register(r'sen5x', Sen5xViewSet, basename='sen5x')
router.register(r'sht10', Sht10ViewSet, basename='sht10')
router.register(r'sht11', Sht11ViewSet, basename='sht11')
router.register(r'sht15', Sht15ViewSet, basename='sht15')
router.register(r'sht30', Sht30ViewSet, basename='sht30')
router.register(r'sht31', Sht31ViewSet, basename='sht31')
router.register(r'sht35', Sht35ViewSet, basename='sht35')
router.register(r'sps30', Sps30ViewSet, basename='sps30')
urlpatterns = [
    path('', include(router.urls)),
]
