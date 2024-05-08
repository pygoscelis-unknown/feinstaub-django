from django.core.management import BaseCommand
import csv
from bs4 import BeautifulSoup
import requests
import urllib.request
from datetime import date
from datetime import timedelta
import time
from .modules.csv import get_header
from .modules.sensor_type_queue import register, skip
import json
import textwrap

class Command(BaseCommand):
    help = "generate models.py from json"

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)
        parser.add_argument('--app', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        apps_name = kwargs['app']

        with open(path) as f:
            data = json.load(f)

            with open("models.py", "w") as pyf:
                pyf.write(textwrap.dedent("""\
                    from django.db import models
                    from django.conf import settings
                    import os
                """))
            with open("admin.py", "w") as pyf:
                pyf.write(textwrap.dedent("""\
                    from django.contrib import admin
                """))

            with open("urls.py", "w") as pyf:
                pyf.write(textwrap.dedent("""\
                    from django.contrib import admin
                    from django.urls import path
                    from django.urls import path, include
                    from django.contrib.auth.models import User
                    from rest_framework import routers, serializers, viewsets
                """))

            with open("create_object.py", "w") as pyf:
                pyf.write("")

            # append content to models.py
            for key, values in data.items():
                key = key.replace("-", "")

                with open("models.py", "a") as pyf:
                    pyf.write(textwrap.dedent("""\
                        class {}(models.Model):
                    """.format(key)))

                    for value in values:
                        if value == "sensor_id"\
                                or value == "location":
                            pyf.write(textwrap.dedent("""\
                            #
                                {} = models.IntegerField(null=True, blank=True)
                            """).format(value))
                        elif value == "sensor_type":
                            pyf.write(textwrap.dedent("""\
                            #
                                {} = models.CharField(max_length=255, blank=True)
                            """).format(value))
                        elif value == "timestamp":
                            pyf.write(textwrap.dedent("""\
                            #
                                {} = models.DateTimeField(null=True, blank=True)
                            """).format(value))
                        else:
                            pyf.write(textwrap.dedent("""\
                            #
                                {} = models.FloatField(null=True, blank=True)
                            """).format(value))

            # append content to admin.py
            for key, values in data.items():
                key = key.replace("-", "")

                with open("admin.py", "a") as pyf:
                    pyf.write(textwrap.dedent("""\
                        from .models import {}
                    """.format(key)))


            for key, values in data.items():
                key = key.replace("-", "")

                with open("admin.py", "a") as pyf:
                    pyf.write(textwrap.dedent("""\
                        admin.site.register({})
                    """.format(key)))

            # append content to urls.py
            for key, value in data.items():
                key = key.replace("-", "")

                with open("urls.py", "a") as pyf:
                    pyf.write(textwrap.dedent("""\
                        from {}.models import {}
                    """.format(apps_name, key)))

            with open("urls.py", "a") as pyf:
                pyf.write(textwrap.dedent("""\
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
                """))

            for key, value in data.items():
                key = key.replace("-", "")

                with open("urls.py", "a") as pyf:
                    pyf.write(textwrap.dedent("""\
                        class {}Serializer(serializers.HyperlinkedModelSerializer):
                            class Meta:
                                model = {}
                                fields = "__all__"
                        class {}ViewSet(viewsets.ModelViewSet):
                            queryset = {}.objects.all()
                            serializer_class = {}Serializer
                        router.register(r'{}', {}ViewSet)
                    """.format(key.capitalize(), key, key.capitalize(), key, key.capitalize(), key, key.capitalize())))

            with open("urls.py", "a") as pyf:
                pyf.write(textwrap.dedent("""\
                    # Wire up our API using automatic URL routing.
                    # Additionally, we include login URLs for the browsable API.
                    urlpatterns = [
                        path('admin/', admin.site.urls),
                        path('', include(router.urls)),
                        path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
                    ]
                """))

            # append content to create_object.py
            for key, values in data.items():
                key = key.replace("-", "")

                with open("create_object.py", "a") as pyf:
                    pyf.write(textwrap.dedent("""\
                        from {}.models import {}
                    """.format(apps_name, key)))

            with open("create_object.py", "a") as pyf:
                pyf.write(textwrap.dedent("""\
                    def create(sensor_type, row):
                """.format(key)))

            for key, values in data.items():
                key = key.replace("-", "")

                with open("create_object.py", "a") as pyf:
                    pyf.write(textwrap.dedent("""\
                    #
                        if sensor_type == "{}":
                            command = {}.objects.create(
                    """.format(key, key)))

                    index = 0
                    for value in values:
                        pyf.write(textwrap.dedent("""\
                        #
                                {}=row[{}],
                        """).format(value, index))
                        index += 1

                    pyf.write(textwrap.dedent("""\
                    #
                            )
                    """))

            with open("create_object.py", "a") as pyf:
                pyf.write(textwrap.dedent("""\
                    #
                        return command
                """))
