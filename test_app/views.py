from rest_framework import viewsets
from .models import bme280, bmp180, bmp280, dht22, ds18b20, hpm, htu21d, laerm, nextpm, pms1003, pms3003, pms5003, pms6003, pms7003, ppd42ns, radiation_sbm19, radiation_sbm20, radiation_si22g, scd30, sds011, sht11, sht15, sht30, sht31, sht35, sht85, sps30
from .serializers import Bme280Serializer, Bmp180Serializer, Bmp280Serializer, Dht22Serializer, Ds18b20Serializer, HpmSerializer, Htu21dSerializer, LaermSerializer, NextpmSerializer, Pms1003Serializer, Pms3003Serializer, Pms5003Serializer, Pms6003Serializer, Pms7003Serializer, Ppd42nsSerializer, Radiation_sbm19Serializer, Radiation_sbm20Serializer, Radiation_si22gSerializer, Scd30Serializer, Sds011Serializer, Sht11Serializer, Sht15Serializer, Sht30Serializer, Sht31Serializer, Sht35Serializer, Sht85Serializer, Sps30Serializer

class Bme280ViewSet(viewsets.ModelViewSet):
    queryset = bme280.objects.all()
    serializer_class = Bme280Serializer


class Bmp180ViewSet(viewsets.ModelViewSet):
    queryset = bmp180.objects.all()
    serializer_class = Bmp180Serializer


class Bmp280ViewSet(viewsets.ModelViewSet):
    queryset = bmp280.objects.all()
    serializer_class = Bmp280Serializer


class Dht22ViewSet(viewsets.ModelViewSet):
    queryset = dht22.objects.all()
    serializer_class = Dht22Serializer


class Ds18b20ViewSet(viewsets.ModelViewSet):
    queryset = ds18b20.objects.all()
    serializer_class = Ds18b20Serializer


class HpmViewSet(viewsets.ModelViewSet):
    queryset = hpm.objects.all()
    serializer_class = HpmSerializer


class Htu21dViewSet(viewsets.ModelViewSet):
    queryset = htu21d.objects.all()
    serializer_class = Htu21dSerializer


class LaermViewSet(viewsets.ModelViewSet):
    queryset = laerm.objects.all()
    serializer_class = LaermSerializer


class NextpmViewSet(viewsets.ModelViewSet):
    queryset = nextpm.objects.all()
    serializer_class = NextpmSerializer


class Pms1003ViewSet(viewsets.ModelViewSet):
    queryset = pms1003.objects.all()
    serializer_class = Pms1003Serializer


class Pms3003ViewSet(viewsets.ModelViewSet):
    queryset = pms3003.objects.all()
    serializer_class = Pms3003Serializer


class Pms5003ViewSet(viewsets.ModelViewSet):
    queryset = pms5003.objects.all()
    serializer_class = Pms5003Serializer


class Pms6003ViewSet(viewsets.ModelViewSet):
    queryset = pms6003.objects.all()
    serializer_class = Pms6003Serializer


class Pms7003ViewSet(viewsets.ModelViewSet):
    queryset = pms7003.objects.all()
    serializer_class = Pms7003Serializer


class Ppd42nsViewSet(viewsets.ModelViewSet):
    queryset = ppd42ns.objects.all()
    serializer_class = Ppd42nsSerializer


class Radiation_sbm19ViewSet(viewsets.ModelViewSet):
    queryset = radiation_sbm19.objects.all()
    serializer_class = Radiation_sbm19Serializer


class Radiation_sbm20ViewSet(viewsets.ModelViewSet):
    queryset = radiation_sbm20.objects.all()
    serializer_class = Radiation_sbm20Serializer


class Radiation_si22gViewSet(viewsets.ModelViewSet):
    queryset = radiation_si22g.objects.all()
    serializer_class = Radiation_si22gSerializer


class Scd30ViewSet(viewsets.ModelViewSet):
    queryset = scd30.objects.all()
    serializer_class = Scd30Serializer


class Sds011ViewSet(viewsets.ModelViewSet):
    queryset = sds011.objects.all()
    serializer_class = Sds011Serializer


class Sht11ViewSet(viewsets.ModelViewSet):
    queryset = sht11.objects.all()
    serializer_class = Sht11Serializer


class Sht15ViewSet(viewsets.ModelViewSet):
    queryset = sht15.objects.all()
    serializer_class = Sht15Serializer


class Sht30ViewSet(viewsets.ModelViewSet):
    queryset = sht30.objects.all()
    serializer_class = Sht30Serializer


class Sht31ViewSet(viewsets.ModelViewSet):
    queryset = sht31.objects.all()
    serializer_class = Sht31Serializer


class Sht35ViewSet(viewsets.ModelViewSet):
    queryset = sht35.objects.all()
    serializer_class = Sht35Serializer


class Sht85ViewSet(viewsets.ModelViewSet):
    queryset = sht85.objects.all()
    serializer_class = Sht85Serializer


class Sps30ViewSet(viewsets.ModelViewSet):
    queryset = sps30.objects.all()
    serializer_class = Sps30Serializer
