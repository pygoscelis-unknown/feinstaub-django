#pylint: skip-file
from django.urls import path, include
from rest_framework import routers
from .views import BME280ViewSet, BMP180ViewSet, BMP280ViewSet, DHT22ViewSet, DS18B20ViewSet, HPMViewSet, HTU21DViewSet, PMS1003ViewSet, PMS3003ViewSet, PMS5003ViewSet, PMS6003ViewSet, PMS7003ViewSet, PPD42NSViewSet, SDS011ViewSet
router = routers.DefaultRouter()
router.register(r'bme280', BME280ViewSet, basename='bme280')
router.register(r'bmp180', BMP180ViewSet, basename='bmp180')
router.register(r'bmp280', BMP280ViewSet, basename='bmp280')
router.register(r'dht22', DHT22ViewSet, basename='dht22')
router.register(r'ds18b20', DS18B20ViewSet, basename='ds18b20')
router.register(r'hpm', HPMViewSet, basename='hpm')
router.register(r'htu21d', HTU21DViewSet, basename='htu21d')
router.register(r'pms1003', PMS1003ViewSet, basename='pms1003')
router.register(r'pms3003', PMS3003ViewSet, basename='pms3003')
router.register(r'pms5003', PMS5003ViewSet, basename='pms5003')
router.register(r'pms6003', PMS6003ViewSet, basename='pms6003')
router.register(r'pms7003', PMS7003ViewSet, basename='pms7003')
router.register(r'ppd42ns', PPD42NSViewSet, basename='ppd42ns')
router.register(r'sds011', SDS011ViewSet, basename='sds011')
urlpatterns = [
    path('', include(router.urls)),
]
