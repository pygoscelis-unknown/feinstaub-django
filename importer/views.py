#pylint: skip-file
from rest_framework import viewsets
from .models import BME280, BMP180, BMP280, DHT22, DS18B20, HPM, HTU21D, PMS1003, PMS3003, PMS5003, PMS6003, PMS7003, PPD42NS, SDS011
from .serializers import BME280Serializer, BMP180Serializer, BMP280Serializer, DHT22Serializer, DS18B20Serializer, HPMSerializer, HTU21DSerializer, PMS1003Serializer, PMS3003Serializer, PMS5003Serializer, PMS6003Serializer, PMS7003Serializer, PPD42NSSerializer, SDS011Serializer
class BME280ViewSet(viewsets.ModelViewSet):
    serializer_class = BME280Serializer
    def get_queryset(self):
        queryset = BME280.objects
        query_params = self.request.query_params
        available_params = [
            "sensor_id",
            "location",
            "lat",
            "lon",
            "year",
            "month",
            "day",
            "hour",
        ]
        intersected_params = list(filter(lambda x: x in query_params, available_params))
        no_params_or_no_values = True
        if (len(intersected_params) != 0):
            for pkey in intersected_params:
                pvalue = query_params.get(pkey)
                if pvalue != "":
                    no_params_or_no_values = False
                    if pkey == "sensor_id":
                        queryset = queryset.filter(sensor_id=pvalue)
                    if pkey == "location":
                        queryset = queryset.filter(location=pvalue)
                    if pkey == "lat":
                        queryset = queryset.filter(lat=pvalue)
                    if pkey == "lon":
                        queryset = queryset.filter(lon=pvalue)
                    if pkey == "year":
                        queryset = queryset.filter(timestamp__year=pvalue)
                    if pkey == "month":
                        queryset = queryset.filter(timestamp__month=pvalue)
                    if pkey == "day":
                        queryset = queryset.filter(timestamp__day=pvalue)
                    if pkey == "hour":
                        queryset = queryset.filter(timestamp__hour=pvalue)
        if no_params_or_no_values:
            queryset = queryset.all()
        if query_params.get('sorted') == "1":
            queryset = queryset.order_by('timestamp')
        return queryset
    def get_view_name(self):
        return "BME280 List"
class BMP180ViewSet(viewsets.ModelViewSet):
    serializer_class = BMP180Serializer
    def get_queryset(self):
        queryset = BMP180.objects
        query_params = self.request.query_params
        available_params = [
            "sensor_id",
            "location",
            "lat",
            "lon",
            "year",
            "month",
            "day",
            "hour",
        ]
        intersected_params = list(filter(lambda x: x in query_params, available_params))
        no_params_or_no_values = True
        if (len(intersected_params) != 0):
            for pkey in intersected_params:
                pvalue = query_params.get(pkey)
                if pvalue != "":
                    no_params_or_no_values = False
                    if pkey == "sensor_id":
                        queryset = queryset.filter(sensor_id=pvalue)
                    if pkey == "location":
                        queryset = queryset.filter(location=pvalue)
                    if pkey == "lat":
                        queryset = queryset.filter(lat=pvalue)
                    if pkey == "lon":
                        queryset = queryset.filter(lon=pvalue)
                    if pkey == "year":
                        queryset = queryset.filter(timestamp__year=pvalue)
                    if pkey == "month":
                        queryset = queryset.filter(timestamp__month=pvalue)
                    if pkey == "day":
                        queryset = queryset.filter(timestamp__day=pvalue)
                    if pkey == "hour":
                        queryset = queryset.filter(timestamp__hour=pvalue)
        if no_params_or_no_values:
            queryset = queryset.all()
        if query_params.get('sorted') == "1":
            queryset = queryset.order_by('timestamp')
        return queryset
    def get_view_name(self):
        return "BMP180 List"
class BMP280ViewSet(viewsets.ModelViewSet):
    serializer_class = BMP280Serializer
    def get_queryset(self):
        queryset = BMP280.objects
        query_params = self.request.query_params
        available_params = [
            "sensor_id",
            "location",
            "lat",
            "lon",
            "year",
            "month",
            "day",
            "hour",
        ]
        intersected_params = list(filter(lambda x: x in query_params, available_params))
        no_params_or_no_values = True
        if (len(intersected_params) != 0):
            for pkey in intersected_params:
                pvalue = query_params.get(pkey)
                if pvalue != "":
                    no_params_or_no_values = False
                    if pkey == "sensor_id":
                        queryset = queryset.filter(sensor_id=pvalue)
                    if pkey == "location":
                        queryset = queryset.filter(location=pvalue)
                    if pkey == "lat":
                        queryset = queryset.filter(lat=pvalue)
                    if pkey == "lon":
                        queryset = queryset.filter(lon=pvalue)
                    if pkey == "year":
                        queryset = queryset.filter(timestamp__year=pvalue)
                    if pkey == "month":
                        queryset = queryset.filter(timestamp__month=pvalue)
                    if pkey == "day":
                        queryset = queryset.filter(timestamp__day=pvalue)
                    if pkey == "hour":
                        queryset = queryset.filter(timestamp__hour=pvalue)
        if no_params_or_no_values:
            queryset = queryset.all()
        if query_params.get('sorted') == "1":
            queryset = queryset.order_by('timestamp')
        return queryset
    def get_view_name(self):
        return "BMP280 List"
class DHT22ViewSet(viewsets.ModelViewSet):
    serializer_class = DHT22Serializer
    def get_queryset(self):
        queryset = DHT22.objects
        query_params = self.request.query_params
        available_params = [
            "sensor_id",
            "location",
            "lat",
            "lon",
            "year",
            "month",
            "day",
            "hour",
        ]
        intersected_params = list(filter(lambda x: x in query_params, available_params))
        no_params_or_no_values = True
        if (len(intersected_params) != 0):
            for pkey in intersected_params:
                pvalue = query_params.get(pkey)
                if pvalue != "":
                    no_params_or_no_values = False
                    if pkey == "sensor_id":
                        queryset = queryset.filter(sensor_id=pvalue)
                    if pkey == "location":
                        queryset = queryset.filter(location=pvalue)
                    if pkey == "lat":
                        queryset = queryset.filter(lat=pvalue)
                    if pkey == "lon":
                        queryset = queryset.filter(lon=pvalue)
                    if pkey == "year":
                        queryset = queryset.filter(timestamp__year=pvalue)
                    if pkey == "month":
                        queryset = queryset.filter(timestamp__month=pvalue)
                    if pkey == "day":
                        queryset = queryset.filter(timestamp__day=pvalue)
                    if pkey == "hour":
                        queryset = queryset.filter(timestamp__hour=pvalue)
        if no_params_or_no_values:
            queryset = queryset.all()
        if query_params.get('sorted') == "1":
            queryset = queryset.order_by('timestamp')
        return queryset
    def get_view_name(self):
        return "DHT22 List"
class DS18B20ViewSet(viewsets.ModelViewSet):
    serializer_class = DS18B20Serializer
    def get_queryset(self):
        queryset = DS18B20.objects
        query_params = self.request.query_params
        available_params = [
            "sensor_id",
            "location",
            "lat",
            "lon",
            "year",
            "month",
            "day",
            "hour",
        ]
        intersected_params = list(filter(lambda x: x in query_params, available_params))
        no_params_or_no_values = True
        if (len(intersected_params) != 0):
            for pkey in intersected_params:
                pvalue = query_params.get(pkey)
                if pvalue != "":
                    no_params_or_no_values = False
                    if pkey == "sensor_id":
                        queryset = queryset.filter(sensor_id=pvalue)
                    if pkey == "location":
                        queryset = queryset.filter(location=pvalue)
                    if pkey == "lat":
                        queryset = queryset.filter(lat=pvalue)
                    if pkey == "lon":
                        queryset = queryset.filter(lon=pvalue)
                    if pkey == "year":
                        queryset = queryset.filter(timestamp__year=pvalue)
                    if pkey == "month":
                        queryset = queryset.filter(timestamp__month=pvalue)
                    if pkey == "day":
                        queryset = queryset.filter(timestamp__day=pvalue)
                    if pkey == "hour":
                        queryset = queryset.filter(timestamp__hour=pvalue)
        if no_params_or_no_values:
            queryset = queryset.all()
        if query_params.get('sorted') == "1":
            queryset = queryset.order_by('timestamp')
        return queryset
    def get_view_name(self):
        return "DS18B20 List"
class HPMViewSet(viewsets.ModelViewSet):
    serializer_class = HPMSerializer
    def get_queryset(self):
        queryset = HPM.objects
        query_params = self.request.query_params
        available_params = [
            "sensor_id",
            "location",
            "lat",
            "lon",
            "year",
            "month",
            "day",
            "hour",
        ]
        intersected_params = list(filter(lambda x: x in query_params, available_params))
        no_params_or_no_values = True
        if (len(intersected_params) != 0):
            for pkey in intersected_params:
                pvalue = query_params.get(pkey)
                if pvalue != "":
                    no_params_or_no_values = False
                    if pkey == "sensor_id":
                        queryset = queryset.filter(sensor_id=pvalue)
                    if pkey == "location":
                        queryset = queryset.filter(location=pvalue)
                    if pkey == "lat":
                        queryset = queryset.filter(lat=pvalue)
                    if pkey == "lon":
                        queryset = queryset.filter(lon=pvalue)
                    if pkey == "year":
                        queryset = queryset.filter(timestamp__year=pvalue)
                    if pkey == "month":
                        queryset = queryset.filter(timestamp__month=pvalue)
                    if pkey == "day":
                        queryset = queryset.filter(timestamp__day=pvalue)
                    if pkey == "hour":
                        queryset = queryset.filter(timestamp__hour=pvalue)
        if no_params_or_no_values:
            queryset = queryset.all()
        if query_params.get('sorted') == "1":
            queryset = queryset.order_by('timestamp')
        return queryset
    def get_view_name(self):
        return "HPM List"
class HTU21DViewSet(viewsets.ModelViewSet):
    serializer_class = HTU21DSerializer
    def get_queryset(self):
        queryset = HTU21D.objects
        query_params = self.request.query_params
        available_params = [
            "sensor_id",
            "location",
            "lat",
            "lon",
            "year",
            "month",
            "day",
            "hour",
        ]
        intersected_params = list(filter(lambda x: x in query_params, available_params))
        no_params_or_no_values = True
        if (len(intersected_params) != 0):
            for pkey in intersected_params:
                pvalue = query_params.get(pkey)
                if pvalue != "":
                    no_params_or_no_values = False
                    if pkey == "sensor_id":
                        queryset = queryset.filter(sensor_id=pvalue)
                    if pkey == "location":
                        queryset = queryset.filter(location=pvalue)
                    if pkey == "lat":
                        queryset = queryset.filter(lat=pvalue)
                    if pkey == "lon":
                        queryset = queryset.filter(lon=pvalue)
                    if pkey == "year":
                        queryset = queryset.filter(timestamp__year=pvalue)
                    if pkey == "month":
                        queryset = queryset.filter(timestamp__month=pvalue)
                    if pkey == "day":
                        queryset = queryset.filter(timestamp__day=pvalue)
                    if pkey == "hour":
                        queryset = queryset.filter(timestamp__hour=pvalue)
        if no_params_or_no_values:
            queryset = queryset.all()
        if query_params.get('sorted') == "1":
            queryset = queryset.order_by('timestamp')
        return queryset
    def get_view_name(self):
        return "HTU21D List"
class PMS1003ViewSet(viewsets.ModelViewSet):
    serializer_class = PMS1003Serializer
    def get_queryset(self):
        queryset = PMS1003.objects
        query_params = self.request.query_params
        available_params = [
            "sensor_id",
            "location",
            "lat",
            "lon",
            "year",
            "month",
            "day",
            "hour",
        ]
        intersected_params = list(filter(lambda x: x in query_params, available_params))
        no_params_or_no_values = True
        if (len(intersected_params) != 0):
            for pkey in intersected_params:
                pvalue = query_params.get(pkey)
                if pvalue != "":
                    no_params_or_no_values = False
                    if pkey == "sensor_id":
                        queryset = queryset.filter(sensor_id=pvalue)
                    if pkey == "location":
                        queryset = queryset.filter(location=pvalue)
                    if pkey == "lat":
                        queryset = queryset.filter(lat=pvalue)
                    if pkey == "lon":
                        queryset = queryset.filter(lon=pvalue)
                    if pkey == "year":
                        queryset = queryset.filter(timestamp__year=pvalue)
                    if pkey == "month":
                        queryset = queryset.filter(timestamp__month=pvalue)
                    if pkey == "day":
                        queryset = queryset.filter(timestamp__day=pvalue)
                    if pkey == "hour":
                        queryset = queryset.filter(timestamp__hour=pvalue)
        if no_params_or_no_values:
            queryset = queryset.all()
        if query_params.get('sorted') == "1":
            queryset = queryset.order_by('timestamp')
        return queryset
    def get_view_name(self):
        return "PMS1003 List"
class PMS3003ViewSet(viewsets.ModelViewSet):
    serializer_class = PMS3003Serializer
    def get_queryset(self):
        queryset = PMS3003.objects
        query_params = self.request.query_params
        available_params = [
            "sensor_id",
            "location",
            "lat",
            "lon",
            "year",
            "month",
            "day",
            "hour",
        ]
        intersected_params = list(filter(lambda x: x in query_params, available_params))
        no_params_or_no_values = True
        if (len(intersected_params) != 0):
            for pkey in intersected_params:
                pvalue = query_params.get(pkey)
                if pvalue != "":
                    no_params_or_no_values = False
                    if pkey == "sensor_id":
                        queryset = queryset.filter(sensor_id=pvalue)
                    if pkey == "location":
                        queryset = queryset.filter(location=pvalue)
                    if pkey == "lat":
                        queryset = queryset.filter(lat=pvalue)
                    if pkey == "lon":
                        queryset = queryset.filter(lon=pvalue)
                    if pkey == "year":
                        queryset = queryset.filter(timestamp__year=pvalue)
                    if pkey == "month":
                        queryset = queryset.filter(timestamp__month=pvalue)
                    if pkey == "day":
                        queryset = queryset.filter(timestamp__day=pvalue)
                    if pkey == "hour":
                        queryset = queryset.filter(timestamp__hour=pvalue)
        if no_params_or_no_values:
            queryset = queryset.all()
        if query_params.get('sorted') == "1":
            queryset = queryset.order_by('timestamp')
        return queryset
    def get_view_name(self):
        return "PMS3003 List"
class PMS5003ViewSet(viewsets.ModelViewSet):
    serializer_class = PMS5003Serializer
    def get_queryset(self):
        queryset = PMS5003.objects
        query_params = self.request.query_params
        available_params = [
            "sensor_id",
            "location",
            "lat",
            "lon",
            "year",
            "month",
            "day",
            "hour",
        ]
        intersected_params = list(filter(lambda x: x in query_params, available_params))
        no_params_or_no_values = True
        if (len(intersected_params) != 0):
            for pkey in intersected_params:
                pvalue = query_params.get(pkey)
                if pvalue != "":
                    no_params_or_no_values = False
                    if pkey == "sensor_id":
                        queryset = queryset.filter(sensor_id=pvalue)
                    if pkey == "location":
                        queryset = queryset.filter(location=pvalue)
                    if pkey == "lat":
                        queryset = queryset.filter(lat=pvalue)
                    if pkey == "lon":
                        queryset = queryset.filter(lon=pvalue)
                    if pkey == "year":
                        queryset = queryset.filter(timestamp__year=pvalue)
                    if pkey == "month":
                        queryset = queryset.filter(timestamp__month=pvalue)
                    if pkey == "day":
                        queryset = queryset.filter(timestamp__day=pvalue)
                    if pkey == "hour":
                        queryset = queryset.filter(timestamp__hour=pvalue)
        if no_params_or_no_values:
            queryset = queryset.all()
        if query_params.get('sorted') == "1":
            queryset = queryset.order_by('timestamp')
        return queryset
    def get_view_name(self):
        return "PMS5003 List"
class PMS6003ViewSet(viewsets.ModelViewSet):
    serializer_class = PMS6003Serializer
    def get_queryset(self):
        queryset = PMS6003.objects
        query_params = self.request.query_params
        available_params = [
            "sensor_id",
            "location",
            "lat",
            "lon",
            "year",
            "month",
            "day",
            "hour",
        ]
        intersected_params = list(filter(lambda x: x in query_params, available_params))
        no_params_or_no_values = True
        if (len(intersected_params) != 0):
            for pkey in intersected_params:
                pvalue = query_params.get(pkey)
                if pvalue != "":
                    no_params_or_no_values = False
                    if pkey == "sensor_id":
                        queryset = queryset.filter(sensor_id=pvalue)
                    if pkey == "location":
                        queryset = queryset.filter(location=pvalue)
                    if pkey == "lat":
                        queryset = queryset.filter(lat=pvalue)
                    if pkey == "lon":
                        queryset = queryset.filter(lon=pvalue)
                    if pkey == "year":
                        queryset = queryset.filter(timestamp__year=pvalue)
                    if pkey == "month":
                        queryset = queryset.filter(timestamp__month=pvalue)
                    if pkey == "day":
                        queryset = queryset.filter(timestamp__day=pvalue)
                    if pkey == "hour":
                        queryset = queryset.filter(timestamp__hour=pvalue)
        if no_params_or_no_values:
            queryset = queryset.all()
        if query_params.get('sorted') == "1":
            queryset = queryset.order_by('timestamp')
        return queryset
    def get_view_name(self):
        return "PMS6003 List"
class PMS7003ViewSet(viewsets.ModelViewSet):
    serializer_class = PMS7003Serializer
    def get_queryset(self):
        queryset = PMS7003.objects
        query_params = self.request.query_params
        available_params = [
            "sensor_id",
            "location",
            "lat",
            "lon",
            "year",
            "month",
            "day",
            "hour",
        ]
        intersected_params = list(filter(lambda x: x in query_params, available_params))
        no_params_or_no_values = True
        if (len(intersected_params) != 0):
            for pkey in intersected_params:
                pvalue = query_params.get(pkey)
                if pvalue != "":
                    no_params_or_no_values = False
                    if pkey == "sensor_id":
                        queryset = queryset.filter(sensor_id=pvalue)
                    if pkey == "location":
                        queryset = queryset.filter(location=pvalue)
                    if pkey == "lat":
                        queryset = queryset.filter(lat=pvalue)
                    if pkey == "lon":
                        queryset = queryset.filter(lon=pvalue)
                    if pkey == "year":
                        queryset = queryset.filter(timestamp__year=pvalue)
                    if pkey == "month":
                        queryset = queryset.filter(timestamp__month=pvalue)
                    if pkey == "day":
                        queryset = queryset.filter(timestamp__day=pvalue)
                    if pkey == "hour":
                        queryset = queryset.filter(timestamp__hour=pvalue)
        if no_params_or_no_values:
            queryset = queryset.all()
        if query_params.get('sorted') == "1":
            queryset = queryset.order_by('timestamp')
        return queryset
    def get_view_name(self):
        return "PMS7003 List"
class PPD42NSViewSet(viewsets.ModelViewSet):
    serializer_class = PPD42NSSerializer
    def get_queryset(self):
        queryset = PPD42NS.objects
        query_params = self.request.query_params
        available_params = [
            "sensor_id",
            "location",
            "lat",
            "lon",
            "year",
            "month",
            "day",
            "hour",
        ]
        intersected_params = list(filter(lambda x: x in query_params, available_params))
        no_params_or_no_values = True
        if (len(intersected_params) != 0):
            for pkey in intersected_params:
                pvalue = query_params.get(pkey)
                if pvalue != "":
                    no_params_or_no_values = False
                    if pkey == "sensor_id":
                        queryset = queryset.filter(sensor_id=pvalue)
                    if pkey == "location":
                        queryset = queryset.filter(location=pvalue)
                    if pkey == "lat":
                        queryset = queryset.filter(lat=pvalue)
                    if pkey == "lon":
                        queryset = queryset.filter(lon=pvalue)
                    if pkey == "year":
                        queryset = queryset.filter(timestamp__year=pvalue)
                    if pkey == "month":
                        queryset = queryset.filter(timestamp__month=pvalue)
                    if pkey == "day":
                        queryset = queryset.filter(timestamp__day=pvalue)
                    if pkey == "hour":
                        queryset = queryset.filter(timestamp__hour=pvalue)
        if no_params_or_no_values:
            queryset = queryset.all()
        if query_params.get('sorted') == "1":
            queryset = queryset.order_by('timestamp')
        return queryset
    def get_view_name(self):
        return "PPD42NS List"
class SDS011ViewSet(viewsets.ModelViewSet):
    serializer_class = SDS011Serializer
    def get_queryset(self):
        queryset = SDS011.objects
        query_params = self.request.query_params
        available_params = [
            "sensor_id",
            "location",
            "lat",
            "lon",
            "year",
            "month",
            "day",
            "hour",
        ]
        intersected_params = list(filter(lambda x: x in query_params, available_params))
        no_params_or_no_values = True
        if (len(intersected_params) != 0):
            for pkey in intersected_params:
                pvalue = query_params.get(pkey)
                if pvalue != "":
                    no_params_or_no_values = False
                    if pkey == "sensor_id":
                        queryset = queryset.filter(sensor_id=pvalue)
                    if pkey == "location":
                        queryset = queryset.filter(location=pvalue)
                    if pkey == "lat":
                        queryset = queryset.filter(lat=pvalue)
                    if pkey == "lon":
                        queryset = queryset.filter(lon=pvalue)
                    if pkey == "year":
                        queryset = queryset.filter(timestamp__year=pvalue)
                    if pkey == "month":
                        queryset = queryset.filter(timestamp__month=pvalue)
                    if pkey == "day":
                        queryset = queryset.filter(timestamp__day=pvalue)
                    if pkey == "hour":
                        queryset = queryset.filter(timestamp__hour=pvalue)
        if no_params_or_no_values:
            queryset = queryset.all()
        if query_params.get('sorted') == "1":
            queryset = queryset.order_by('timestamp')
        return queryset
    def get_view_name(self):
        return "SDS011 List"
