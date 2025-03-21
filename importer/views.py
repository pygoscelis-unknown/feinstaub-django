#pylint: skip-file
from rest_framework import viewsets
from .models import BME280, BMP180, BMP280, DHT22, DS18B20, HPM, HTU21D, PMS1003, PMS3003, PMS5003, PMS6003, PMS7003, PPD42NS, SDS011
from .serializers import BME280Serializer, BMP180Serializer, BMP280Serializer, DHT22Serializer, DS18B20Serializer, HPMSerializer, HTU21DSerializer, PMS1003Serializer, PMS3003Serializer, PMS5003Serializer, PMS6003Serializer, PMS7003Serializer, PPD42NSSerializer, SDS011Serializer
class BME280ViewSet(viewsets.ModelViewSet):
    serializer_class = BME280Serializer
    def get_queryset(self):
        queryset = BME280.objects.all()
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
class BMP180ViewSet(viewsets.ModelViewSet):
    serializer_class = BMP180Serializer
    def get_queryset(self):
        queryset = BMP180.objects.all()
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
class BMP280ViewSet(viewsets.ModelViewSet):
    serializer_class = BMP280Serializer
    def get_queryset(self):
        queryset = BMP280.objects.all()
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
class DHT22ViewSet(viewsets.ModelViewSet):
    serializer_class = DHT22Serializer
    def get_queryset(self):
        queryset = DHT22.objects.all()
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
class DS18B20ViewSet(viewsets.ModelViewSet):
    serializer_class = DS18B20Serializer
    def get_queryset(self):
        queryset = DS18B20.objects.all()
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
class HPMViewSet(viewsets.ModelViewSet):
    serializer_class = HPMSerializer
    def get_queryset(self):
        queryset = HPM.objects.all()
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
class HTU21DViewSet(viewsets.ModelViewSet):
    serializer_class = HTU21DSerializer
    def get_queryset(self):
        queryset = HTU21D.objects.all()
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
class PMS1003ViewSet(viewsets.ModelViewSet):
    serializer_class = PMS1003Serializer
    def get_queryset(self):
        queryset = PMS1003.objects.all()
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
class PMS3003ViewSet(viewsets.ModelViewSet):
    serializer_class = PMS3003Serializer
    def get_queryset(self):
        queryset = PMS3003.objects.all()
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
class PMS5003ViewSet(viewsets.ModelViewSet):
    serializer_class = PMS5003Serializer
    def get_queryset(self):
        queryset = PMS5003.objects.all()
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
class PMS6003ViewSet(viewsets.ModelViewSet):
    serializer_class = PMS6003Serializer
    def get_queryset(self):
        queryset = PMS6003.objects.all()
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
class PMS7003ViewSet(viewsets.ModelViewSet):
    serializer_class = PMS7003Serializer
    def get_queryset(self):
        queryset = PMS7003.objects.all()
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
class PPD42NSViewSet(viewsets.ModelViewSet):
    serializer_class = PPD42NSSerializer
    def get_queryset(self):
        queryset = PPD42NS.objects.all()
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
class SDS011ViewSet(viewsets.ModelViewSet):
    serializer_class = SDS011Serializer
    def get_queryset(self):
        queryset = SDS011.objects.all()
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
