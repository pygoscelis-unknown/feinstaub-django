#pylint: skip-file
from rest_framework import serializers
from .models import bme280, bmp180, bmp280, dht22, ds18b20, hpm, htu21d, pms1003, pms3003, pms5003, pms6003, pms7003, ppd42ns, sds011
class Bme280Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bme280
        fields = "__all__"
class Bmp180Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bmp180
        fields = "__all__"
class Bmp280Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bmp280
        fields = "__all__"
class Dht22Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = dht22
        fields = "__all__"
class Ds18b20Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ds18b20
        fields = "__all__"
class HpmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = hpm
        fields = "__all__"
class Htu21dSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = htu21d
        fields = "__all__"
class Pms1003Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pms1003
        fields = "__all__"
class Pms3003Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pms3003
        fields = "__all__"
class Pms5003Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pms5003
        fields = "__all__"
class Pms6003Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pms6003
        fields = "__all__"
class Pms7003Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pms7003
        fields = "__all__"
class Ppd42nsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ppd42ns
        fields = "__all__"
class Sds011Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sds011
        fields = "__all__"
