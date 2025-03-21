#pylint: skip-file
from rest_framework import serializers
from .models import BME280, BMP180, BMP280, DHT22, DS18B20, HPM, HTU21D, PMS1003, PMS3003, PMS5003, PMS6003, PMS7003, PPD42NS, SDS011
class BME280Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BME280
        fields = "__all__"
class BMP180Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BMP180
        fields = "__all__"
class BMP280Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BMP280
        fields = "__all__"
class DHT22Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DHT22
        fields = "__all__"
class DS18B20Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DS18B20
        fields = "__all__"
class HPMSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HPM
        fields = "__all__"
class HTU21DSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HTU21D
        fields = "__all__"
class PMS1003Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PMS1003
        fields = "__all__"
class PMS3003Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PMS3003
        fields = "__all__"
class PMS5003Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PMS5003
        fields = "__all__"
class PMS6003Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PMS6003
        fields = "__all__"
class PMS7003Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PMS7003
        fields = "__all__"
class PPD42NSSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PPD42NS
        fields = "__all__"
class SDS011Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SDS011
        fields = "__all__"
