from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from test_app.models import bme280
from test_app.models import bmp180
from test_app.models import bmp280
from test_app.models import dht22
from test_app.models import ds18b20
from test_app.models import hpm
from test_app.models import htu21d
from test_app.models import laerm
from test_app.models import nextpm
from test_app.models import pms1003
from test_app.models import pms3003
from test_app.models import pms5003
from test_app.models import pms6003
from test_app.models import pms7003
from test_app.models import ppd42ns
from test_app.models import radiation_sbm19
from test_app.models import radiation_sbm20
from test_app.models import radiation_si22g
from test_app.models import scd30
from test_app.models import sds011
from test_app.models import sht11
from test_app.models import sht15
from test_app.models import sht30
from test_app.models import sht31
from test_app.models import sht35
from test_app.models import sht85
from test_app.models import sps30
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
class Bme280Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bme280
        fields = "__all__"
class Bme280ViewSet(viewsets.ModelViewSet):
    queryset = bme280.objects.all()
    serializer_class = Bme280Serializer
router.register(r'bme280', Bme280ViewSet)
class Bmp180Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bmp180
        fields = "__all__"
class Bmp180ViewSet(viewsets.ModelViewSet):
    queryset = bmp180.objects.all()
    serializer_class = Bmp180Serializer
router.register(r'bmp180', Bmp180ViewSet)
class Bmp280Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bmp280
        fields = "__all__"
class Bmp280ViewSet(viewsets.ModelViewSet):
    queryset = bmp280.objects.all()
    serializer_class = Bmp280Serializer
router.register(r'bmp280', Bmp280ViewSet)
class Dht22Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = dht22
        fields = "__all__"
class Dht22ViewSet(viewsets.ModelViewSet):
    queryset = dht22.objects.all()
    serializer_class = Dht22Serializer
router.register(r'dht22', Dht22ViewSet)
class Ds18b20Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ds18b20
        fields = "__all__"
class Ds18b20ViewSet(viewsets.ModelViewSet):
    queryset = ds18b20.objects.all()
    serializer_class = Ds18b20Serializer
router.register(r'ds18b20', Ds18b20ViewSet)
class HpmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = hpm
        fields = "__all__"
class HpmViewSet(viewsets.ModelViewSet):
    queryset = hpm.objects.all()
    serializer_class = HpmSerializer
router.register(r'hpm', HpmViewSet)
class Htu21dSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = htu21d
        fields = "__all__"
class Htu21dViewSet(viewsets.ModelViewSet):
    queryset = htu21d.objects.all()
    serializer_class = Htu21dSerializer
router.register(r'htu21d', Htu21dViewSet)
class LaermSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = laerm
        fields = "__all__"
class LaermViewSet(viewsets.ModelViewSet):
    queryset = laerm.objects.all()
    serializer_class = LaermSerializer
router.register(r'laerm', LaermViewSet)
class NextpmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = nextpm
        fields = "__all__"
class NextpmViewSet(viewsets.ModelViewSet):
    queryset = nextpm.objects.all()
    serializer_class = NextpmSerializer
router.register(r'nextpm', NextpmViewSet)
class Pms1003Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pms1003
        fields = "__all__"
class Pms1003ViewSet(viewsets.ModelViewSet):
    queryset = pms1003.objects.all()
    serializer_class = Pms1003Serializer
router.register(r'pms1003', Pms1003ViewSet)
class Pms3003Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pms3003
        fields = "__all__"
class Pms3003ViewSet(viewsets.ModelViewSet):
    queryset = pms3003.objects.all()
    serializer_class = Pms3003Serializer
router.register(r'pms3003', Pms3003ViewSet)
class Pms5003Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pms5003
        fields = "__all__"
class Pms5003ViewSet(viewsets.ModelViewSet):
    queryset = pms5003.objects.all()
    serializer_class = Pms5003Serializer
router.register(r'pms5003', Pms5003ViewSet)
class Pms6003Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pms6003
        fields = "__all__"
class Pms6003ViewSet(viewsets.ModelViewSet):
    queryset = pms6003.objects.all()
    serializer_class = Pms6003Serializer
router.register(r'pms6003', Pms6003ViewSet)
class Pms7003Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pms7003
        fields = "__all__"
class Pms7003ViewSet(viewsets.ModelViewSet):
    queryset = pms7003.objects.all()
    serializer_class = Pms7003Serializer
router.register(r'pms7003', Pms7003ViewSet)
class Ppd42nsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ppd42ns
        fields = "__all__"
class Ppd42nsViewSet(viewsets.ModelViewSet):
    queryset = ppd42ns.objects.all()
    serializer_class = Ppd42nsSerializer
router.register(r'ppd42ns', Ppd42nsViewSet)
class Radiation_sbm19Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = radiation_sbm19
        fields = "__all__"
class Radiation_sbm19ViewSet(viewsets.ModelViewSet):
    queryset = radiation_sbm19.objects.all()
    serializer_class = Radiation_sbm19Serializer
router.register(r'radiation_sbm19', Radiation_sbm19ViewSet)
class Radiation_sbm20Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = radiation_sbm20
        fields = "__all__"
class Radiation_sbm20ViewSet(viewsets.ModelViewSet):
    queryset = radiation_sbm20.objects.all()
    serializer_class = Radiation_sbm20Serializer
router.register(r'radiation_sbm20', Radiation_sbm20ViewSet)
class Radiation_si22gSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = radiation_si22g
        fields = "__all__"
class Radiation_si22gViewSet(viewsets.ModelViewSet):
    queryset = radiation_si22g.objects.all()
    serializer_class = Radiation_si22gSerializer
router.register(r'radiation_si22g', Radiation_si22gViewSet)
class Scd30Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = scd30
        fields = "__all__"
class Scd30ViewSet(viewsets.ModelViewSet):
    queryset = scd30.objects.all()
    serializer_class = Scd30Serializer
router.register(r'scd30', Scd30ViewSet)
class Sds011Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sds011
        fields = "__all__"
class Sds011ViewSet(viewsets.ModelViewSet):
    queryset = sds011.objects.all()
    serializer_class = Sds011Serializer
router.register(r'sds011', Sds011ViewSet)
class Sht11Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sht11
        fields = "__all__"
class Sht11ViewSet(viewsets.ModelViewSet):
    queryset = sht11.objects.all()
    serializer_class = Sht11Serializer
router.register(r'sht11', Sht11ViewSet)
class Sht15Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sht15
        fields = "__all__"
class Sht15ViewSet(viewsets.ModelViewSet):
    queryset = sht15.objects.all()
    serializer_class = Sht15Serializer
router.register(r'sht15', Sht15ViewSet)
class Sht30Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sht30
        fields = "__all__"
class Sht30ViewSet(viewsets.ModelViewSet):
    queryset = sht30.objects.all()
    serializer_class = Sht30Serializer
router.register(r'sht30', Sht30ViewSet)
class Sht31Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sht31
        fields = "__all__"
class Sht31ViewSet(viewsets.ModelViewSet):
    queryset = sht31.objects.all()
    serializer_class = Sht31Serializer
router.register(r'sht31', Sht31ViewSet)
class Sht35Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sht35
        fields = "__all__"
class Sht35ViewSet(viewsets.ModelViewSet):
    queryset = sht35.objects.all()
    serializer_class = Sht35Serializer
router.register(r'sht35', Sht35ViewSet)
class Sht85Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sht85
        fields = "__all__"
class Sht85ViewSet(viewsets.ModelViewSet):
    queryset = sht85.objects.all()
    serializer_class = Sht85Serializer
router.register(r'sht85', Sht85ViewSet)
class Sps30Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sps30
        fields = "__all__"
class Sps30ViewSet(viewsets.ModelViewSet):
    queryset = sps30.objects.all()
    serializer_class = Sps30Serializer
router.register(r'sps30', Sps30ViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
