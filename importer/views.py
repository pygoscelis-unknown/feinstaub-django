#pylint: skip-file
from rest_framework import viewsets
from .models import bme280, bmp180, bmp280, dht22, ds18b20, hpm, htu21d, pms1003, pms3003, pms5003, pms6003, pms7003, ppd42ns, sds011
from .serializers import Bme280Serializer, Bmp180Serializer, Bmp280Serializer, Dht22Serializer, Ds18b20Serializer, HpmSerializer, Htu21dSerializer, Pms1003Serializer, Pms3003Serializer, Pms5003Serializer, Pms6003Serializer, Pms7003Serializer, Ppd42nsSerializer, Sds011Serializer
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
        queried_lat = self.request.query_params.get("lat")
        if queried_lat is not None:
            queryset = queryset.filter(lat=queried_lat)
        queried_lon = self.request.query_params.get("lon")
        if queried_lon is not None:
            queryset = queryset.filter(lon=queried_lon)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        queried_hour = self.request.query_params.get("hour")
        if queried_hour is not None:
            queryset = queryset.filter(timestamp__hour=queried_hour)
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
        queried_lat = self.request.query_params.get("lat")
        if queried_lat is not None:
            queryset = queryset.filter(lat=queried_lat)
        queried_lon = self.request.query_params.get("lon")
        if queried_lon is not None:
            queryset = queryset.filter(lon=queried_lon)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        queried_hour = self.request.query_params.get("hour")
        if queried_hour is not None:
            queryset = queryset.filter(timestamp__hour=queried_hour)
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
        queried_lat = self.request.query_params.get("lat")
        if queried_lat is not None:
            queryset = queryset.filter(lat=queried_lat)
        queried_lon = self.request.query_params.get("lon")
        if queried_lon is not None:
            queryset = queryset.filter(lon=queried_lon)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        queried_hour = self.request.query_params.get("hour")
        if queried_hour is not None:
            queryset = queryset.filter(timestamp__hour=queried_hour)
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
        queried_lat = self.request.query_params.get("lat")
        if queried_lat is not None:
            queryset = queryset.filter(lat=queried_lat)
        queried_lon = self.request.query_params.get("lon")
        if queried_lon is not None:
            queryset = queryset.filter(lon=queried_lon)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        queried_hour = self.request.query_params.get("hour")
        if queried_hour is not None:
            queryset = queryset.filter(timestamp__hour=queried_hour)
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
        queried_lat = self.request.query_params.get("lat")
        if queried_lat is not None:
            queryset = queryset.filter(lat=queried_lat)
        queried_lon = self.request.query_params.get("lon")
        if queried_lon is not None:
            queryset = queryset.filter(lon=queried_lon)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        queried_hour = self.request.query_params.get("hour")
        if queried_hour is not None:
            queryset = queryset.filter(timestamp__hour=queried_hour)
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
        queried_lat = self.request.query_params.get("lat")
        if queried_lat is not None:
            queryset = queryset.filter(lat=queried_lat)
        queried_lon = self.request.query_params.get("lon")
        if queried_lon is not None:
            queryset = queryset.filter(lon=queried_lon)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        queried_hour = self.request.query_params.get("hour")
        if queried_hour is not None:
            queryset = queryset.filter(timestamp__hour=queried_hour)
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
        queried_lat = self.request.query_params.get("lat")
        if queried_lat is not None:
            queryset = queryset.filter(lat=queried_lat)
        queried_lon = self.request.query_params.get("lon")
        if queried_lon is not None:
            queryset = queryset.filter(lon=queried_lon)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        queried_hour = self.request.query_params.get("hour")
        if queried_hour is not None:
            queryset = queryset.filter(timestamp__hour=queried_hour)
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
        queried_lat = self.request.query_params.get("lat")
        if queried_lat is not None:
            queryset = queryset.filter(lat=queried_lat)
        queried_lon = self.request.query_params.get("lon")
        if queried_lon is not None:
            queryset = queryset.filter(lon=queried_lon)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        queried_hour = self.request.query_params.get("hour")
        if queried_hour is not None:
            queryset = queryset.filter(timestamp__hour=queried_hour)
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
        queried_lat = self.request.query_params.get("lat")
        if queried_lat is not None:
            queryset = queryset.filter(lat=queried_lat)
        queried_lon = self.request.query_params.get("lon")
        if queried_lon is not None:
            queryset = queryset.filter(lon=queried_lon)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        queried_hour = self.request.query_params.get("hour")
        if queried_hour is not None:
            queryset = queryset.filter(timestamp__hour=queried_hour)
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
        queried_lat = self.request.query_params.get("lat")
        if queried_lat is not None:
            queryset = queryset.filter(lat=queried_lat)
        queried_lon = self.request.query_params.get("lon")
        if queried_lon is not None:
            queryset = queryset.filter(lon=queried_lon)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        queried_hour = self.request.query_params.get("hour")
        if queried_hour is not None:
            queryset = queryset.filter(timestamp__hour=queried_hour)
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
        queried_lat = self.request.query_params.get("lat")
        if queried_lat is not None:
            queryset = queryset.filter(lat=queried_lat)
        queried_lon = self.request.query_params.get("lon")
        if queried_lon is not None:
            queryset = queryset.filter(lon=queried_lon)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        queried_hour = self.request.query_params.get("hour")
        if queried_hour is not None:
            queryset = queryset.filter(timestamp__hour=queried_hour)
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
        queried_lat = self.request.query_params.get("lat")
        if queried_lat is not None:
            queryset = queryset.filter(lat=queried_lat)
        queried_lon = self.request.query_params.get("lon")
        if queried_lon is not None:
            queryset = queryset.filter(lon=queried_lon)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        queried_hour = self.request.query_params.get("hour")
        if queried_hour is not None:
            queryset = queryset.filter(timestamp__hour=queried_hour)
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
        queried_lat = self.request.query_params.get("lat")
        if queried_lat is not None:
            queryset = queryset.filter(lat=queried_lat)
        queried_lon = self.request.query_params.get("lon")
        if queried_lon is not None:
            queryset = queryset.filter(lon=queried_lon)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        queried_hour = self.request.query_params.get("hour")
        if queried_hour is not None:
            queryset = queryset.filter(timestamp__hour=queried_hour)
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
        queried_lat = self.request.query_params.get("lat")
        if queried_lat is not None:
            queryset = queryset.filter(lat=queried_lat)
        queried_lon = self.request.query_params.get("lon")
        if queried_lon is not None:
            queryset = queryset.filter(lon=queried_lon)
        queried_year = self.request.query_params.get("year")
        if queried_year is not None:
            queryset = queryset.filter(timestamp__year=queried_year)
        queried_month = self.request.query_params.get("month")
        if queried_month is not None:
            queryset = queryset.filter(timestamp__month=queried_month)
        queried_day = self.request.query_params.get("day")
        if queried_day is not None:
            queryset = queryset.filter(timestamp__day=queried_day)
        queried_hour = self.request.query_params.get("hour")
        if queried_hour is not None:
            queryset = queryset.filter(timestamp__hour=queried_hour)
        return queryset
