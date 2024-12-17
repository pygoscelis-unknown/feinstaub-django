#pylint: skip-file
from rest_framework import viewsets
from .models import bme280, bmp180, bmp280, dht22, ds18b20, hpm, htu21d, laerm, nextpm, pms1003, pms3003, pms5003, pms6003, pms7003, ppd42ns, radiation_sbm19, radiation_sbm20, radiation_si22g, scd30, sds011, sen5x, sht10, sht11, sht15, sht30, sht31, sht35, sht85, sps30
from .serializers import Bme280Serializer, Bmp180Serializer, Bmp280Serializer, Dht22Serializer, Ds18b20Serializer, HpmSerializer, Htu21dSerializer, LaermSerializer, NextpmSerializer, Pms1003Serializer, Pms3003Serializer, Pms5003Serializer, Pms6003Serializer, Pms7003Serializer, Ppd42nsSerializer, Radiation_sbm19Serializer, Radiation_sbm20Serializer, Radiation_si22gSerializer, Scd30Serializer, Sds011Serializer, Sen5xSerializer, Sht10Serializer, Sht11Serializer, Sht15Serializer, Sht30Serializer, Sht31Serializer, Sht35Serializer, Sht85Serializer, Sps30Serializer
class Bme280ViewSet(viewsets.ModelViewSet):
    serializer_class = Bme280Serializer
    def get_queryset(self):
        queryset = bme280.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Bmp180ViewSet(viewsets.ModelViewSet):
    serializer_class = Bmp180Serializer
    def get_queryset(self):
        queryset = bmp180.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Bmp280ViewSet(viewsets.ModelViewSet):
    serializer_class = Bmp280Serializer
    def get_queryset(self):
        queryset = bmp280.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Dht22ViewSet(viewsets.ModelViewSet):
    serializer_class = Dht22Serializer
    def get_queryset(self):
        queryset = dht22.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Ds18b20ViewSet(viewsets.ModelViewSet):
    serializer_class = Ds18b20Serializer
    def get_queryset(self):
        queryset = ds18b20.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class HpmViewSet(viewsets.ModelViewSet):
    serializer_class = HpmSerializer
    def get_queryset(self):
        queryset = hpm.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Htu21dViewSet(viewsets.ModelViewSet):
    serializer_class = Htu21dSerializer
    def get_queryset(self):
        queryset = htu21d.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class LaermViewSet(viewsets.ModelViewSet):
    serializer_class = LaermSerializer
    def get_queryset(self):
        queryset = laerm.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class NextpmViewSet(viewsets.ModelViewSet):
    serializer_class = NextpmSerializer
    def get_queryset(self):
        queryset = nextpm.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Pms1003ViewSet(viewsets.ModelViewSet):
    serializer_class = Pms1003Serializer
    def get_queryset(self):
        queryset = pms1003.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Pms3003ViewSet(viewsets.ModelViewSet):
    serializer_class = Pms3003Serializer
    def get_queryset(self):
        queryset = pms3003.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Pms5003ViewSet(viewsets.ModelViewSet):
    serializer_class = Pms5003Serializer
    def get_queryset(self):
        queryset = pms5003.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Pms6003ViewSet(viewsets.ModelViewSet):
    serializer_class = Pms6003Serializer
    def get_queryset(self):
        queryset = pms6003.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Pms7003ViewSet(viewsets.ModelViewSet):
    serializer_class = Pms7003Serializer
    def get_queryset(self):
        queryset = pms7003.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Ppd42nsViewSet(viewsets.ModelViewSet):
    serializer_class = Ppd42nsSerializer
    def get_queryset(self):
        queryset = ppd42ns.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Radiation_sbm19ViewSet(viewsets.ModelViewSet):
    serializer_class = Radiation_sbm19Serializer
    def get_queryset(self):
        queryset = radiation_sbm19.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Radiation_sbm20ViewSet(viewsets.ModelViewSet):
    serializer_class = Radiation_sbm20Serializer
    def get_queryset(self):
        queryset = radiation_sbm20.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Radiation_si22gViewSet(viewsets.ModelViewSet):
    serializer_class = Radiation_si22gSerializer
    def get_queryset(self):
        queryset = radiation_si22g.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Scd30ViewSet(viewsets.ModelViewSet):
    serializer_class = Scd30Serializer
    def get_queryset(self):
        queryset = scd30.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Sds011ViewSet(viewsets.ModelViewSet):
    serializer_class = Sds011Serializer
    def get_queryset(self):
        queryset = sds011.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Sen5xViewSet(viewsets.ModelViewSet):
    serializer_class = Sen5xSerializer
    def get_queryset(self):
        queryset = sen5x.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Sht10ViewSet(viewsets.ModelViewSet):
    serializer_class = Sht10Serializer
    def get_queryset(self):
        queryset = sht10.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Sht11ViewSet(viewsets.ModelViewSet):
    serializer_class = Sht11Serializer
    def get_queryset(self):
        queryset = sht11.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Sht15ViewSet(viewsets.ModelViewSet):
    serializer_class = Sht15Serializer
    def get_queryset(self):
        queryset = sht15.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Sht30ViewSet(viewsets.ModelViewSet):
    serializer_class = Sht30Serializer
    def get_queryset(self):
        queryset = sht30.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Sht31ViewSet(viewsets.ModelViewSet):
    serializer_class = Sht31Serializer
    def get_queryset(self):
        queryset = sht31.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Sht35ViewSet(viewsets.ModelViewSet):
    serializer_class = Sht35Serializer
    def get_queryset(self):
        queryset = sht35.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Sht85ViewSet(viewsets.ModelViewSet):
    serializer_class = Sht85Serializer
    def get_queryset(self):
        queryset = sht85.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
class Sps30ViewSet(viewsets.ModelViewSet):
    serializer_class = Sps30Serializer
    def get_queryset(self):
        queryset = sps30.objects.all()
        queried_sensor_id = self.request.query_params.get("sensor_id")
        if queried_sensor_id is not None:
            queryset = queryset.filter(sensor_id=queried_sensor_id)
        queried_location = self.request.query_params.get("location")
        if queried_location is not None:
            queryset = queryset.filter(location=queried_location)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        return queryset
