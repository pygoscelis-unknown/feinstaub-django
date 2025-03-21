#pylint: skip-file
from django.urls import path, include
from rest_framework import routers
from .views import BME280ViewSet, BMP180ViewSet, BMP280ViewSet, DHT22ViewSet, DS18B20ViewSet, HPMViewSet, HTU21DViewSet, PMS1003ViewSet, PMS3003ViewSet, PMS5003ViewSet, PMS6003ViewSet, PMS7003ViewSet, PPD42NSViewSet, SDS011ViewSet
router = routers.DefaultRouter()
router.register(r'bme280', BME280ViewSet, basename='BME280')
router.register(r'bmp180', BMP180ViewSet, basename='BMP180')
router.register(r'bmp280', BMP280ViewSet, basename='BMP280')
router.register(r'dht22', DHT22ViewSet, basename='DHT22')
router.register(r'ds18b20', DS18B20ViewSet, basename='DS18B20')
router.register(r'hpm', HPMViewSet, basename='HPM')
router.register(r'htu21d', HTU21DViewSet, basename='HTU21D')
router.register(r'pms1003', PMS1003ViewSet, basename='PMS1003')
router.register(r'pms3003', PMS3003ViewSet, basename='PMS3003')
router.register(r'pms5003', PMS5003ViewSet, basename='PMS5003')
router.register(r'pms6003', PMS6003ViewSet, basename='PMS6003')
router.register(r'pms7003', PMS7003ViewSet, basename='PMS7003')
router.register(r'ppd42ns', PPD42NSViewSet, basename='PPD42NS')
router.register(r'sds011', SDS011ViewSet, basename='SDS011')
urlpatterns = [
    path('', include(router.urls)),
]
