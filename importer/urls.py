#pylint: skip-file
from django.urls import path, include
from rest_framework import routers
from .views import Bme280ViewSet, Bmp180ViewSet, Bmp280ViewSet, Dht22ViewSet, Ds18b20ViewSet, HpmViewSet, Htu21dViewSet, Pms1003ViewSet, Pms3003ViewSet, Pms5003ViewSet, Pms6003ViewSet, Pms7003ViewSet, Ppd42nsViewSet, Sds011ViewSet
router = routers.DefaultRouter()
router.register(r'bme280', Bme280ViewSet, basename='bme280')
router.register(r'bmp180', Bmp180ViewSet, basename='bmp180')
router.register(r'bmp280', Bmp280ViewSet, basename='bmp280')
router.register(r'dht22', Dht22ViewSet, basename='dht22')
router.register(r'ds18b20', Ds18b20ViewSet, basename='ds18b20')
router.register(r'hpm', HpmViewSet, basename='hpm')
router.register(r'htu21d', Htu21dViewSet, basename='htu21d')
router.register(r'pms1003', Pms1003ViewSet, basename='pms1003')
router.register(r'pms3003', Pms3003ViewSet, basename='pms3003')
router.register(r'pms5003', Pms5003ViewSet, basename='pms5003')
router.register(r'pms6003', Pms6003ViewSet, basename='pms6003')
router.register(r'pms7003', Pms7003ViewSet, basename='pms7003')
router.register(r'ppd42ns', Ppd42nsViewSet, basename='ppd42ns')
router.register(r'sds011', Sds011ViewSet, basename='sds011')
urlpatterns = [
    path('', include(router.urls)),
]
