from rest_framework import serializers
from .models import bme280, bmp180, bmp280, dht22, ds18b20, hpm, htu21d, laerm, nextpm, pms1003, pms3003, pms5003, pms6003, pms7003, ppd42ns, radiation_sbm19, radiation_sbm20, radiation_si22g, scd30, sds011, sht11, sht15, sht30, sht31, sht35, sht85, sps30

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


class LaermSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = laerm
        fields = "__all__"


class NextpmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = nextpm
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


class Radiation_sbm19Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = radiation_sbm19
        fields = "__all__"


class Radiation_sbm20Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = radiation_sbm20
        fields = "__all__"


class Radiation_si22gSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = radiation_si22g
        fields = "__all__"


class Scd30Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = scd30
        fields = "__all__"


class Sds011Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sds011
        fields = "__all__"


class Sht11Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sht11
        fields = "__all__"


class Sht15Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sht15
        fields = "__all__"


class Sht30Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sht30
        fields = "__all__"


class Sht31Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sht31
        fields = "__all__"


class Sht35Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sht35
        fields = "__all__"


class Sht85Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sht85
        fields = "__all__"


class Sps30Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sps30
        fields = "__all__"
