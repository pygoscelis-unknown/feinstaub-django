import os
import json
import textwrap
from dotenv import load_dotenv
from django.core.management import BaseCommand


class Command(BaseCommand):
    """
    Generates base config files for importer app and
    moves these files automatically into app/project folder.
    """

    help = """
    Generates app base config files from csv header json.
    """

    def add_arguments(self, parser):
        parser.add_argument('--json', type=str, help="Path to header json file")

    def handle(self, *args, **kwargs):
        load_dotenv()
        json_file = kwargs['json']
        project_name = os.environ.get("DJANGO_PROJECT_NAME")
        app_name = os.environ.get("DJANGO_APP_NAME")

        # --- GET HEADER DATA --- #
        with open(json_file, encoding="utf-8") as f:
            data = json.load(f)

        # --- INIT FILES --- #
        app_basefiles = [
            "models.py",
            "admin.py",
            "serializers.py",
            "views.py",
            "urls.py"
        ]

        app_commandfiles = [
            "create_object.py"
        ]

        project_filenames = [
            "p_urls.py"
        ]

        for files in [app_basefiles, app_commandfiles, project_filenames]:
            for file in files:
                with open(file, "w", encoding="utf-8") as pyf:
                    pyf.write(textwrap.dedent("""\
                        #pylint: skip-file
                    """))

        with open(app_basefiles[0], "a", encoding="utf-8") as pyf:
            pyf.write(textwrap.dedent("""\
                from django.db import models
            """))

        with open(app_basefiles[1], "a", encoding="utf-8") as pyf:
            pyf.write(textwrap.dedent("""\
                from django.contrib import admin
            """))

        with open(app_basefiles[2], "a", encoding="utf-8") as pyf:
            pyf.write(textwrap.dedent("""\
                from rest_framework import serializers
            """))

        with open(app_basefiles[3], "a", encoding="utf-8") as pyf:
            pyf.write(textwrap.dedent("""\
                from rest_framework import viewsets
            """))

        with open(app_basefiles[4], "a", encoding="utf-8") as pyf:
            pyf.write(textwrap.dedent("""\
                from django.urls import path, include
                from rest_framework import routers
            """))

        with open(project_filenames[0], "a", encoding="utf-8") as pyf:
            pyf.write(textwrap.dedent("""\
                from django.contrib import admin
                from django.urls import path, include
                from django.contrib.auth.models import User
                from rest_framework import routers, serializers, viewsets
            """))

        with open(app_commandfiles[0], "a", encoding="utf-8") as pyf:
            pyf.write(textwrap.dedent("""\
                import django
                django.setup()
            """))

        # --- ITERATE OVER OBJECTS --- #
        index = 0
        for key, values in data.items():
            key = key.replace("-", "")

            with open(app_basefiles[0], "a", encoding="utf-8") as pyf:
                pyf.write(textwrap.dedent(f"""\
                    class {key}(models.Model):
                """))

                for value in values:
                    if value in ("sensor_id", "location"):
                        pyf.write(textwrap.dedent(f"""\
                        #
                            {value} = models.IntegerField(null=True, blank=True)
                        """))
                    elif value == "sensor_type":
                        pyf.write(textwrap.dedent(f"""\
                        #
                            {value} = models.CharField(max_length=255, blank=True)
                        """))
                    elif value == "timestamp":
                        pyf.write(textwrap.dedent(f"""\
                        #
                            {value} = models.DateTimeField(null=True, blank=True)
                        """))
                    else:
                        pyf.write(textwrap.dedent(f"""\
                        #
                            {value} = models.FloatField(null=True, blank=True)
                        """))

            # --- IMPORT MODELS --- #
            with open(app_basefiles[1], "a", encoding="utf-8") as pyf:
                if index == 0:
                    pyf.write(f"from .models import {key}")
                else:
                    if index == len(data) - 1:
                        pyf.write(f", {key}\n")
                    else:
                        pyf.write(f", {key}")

            with open(app_basefiles[2], "a", encoding="utf-8") as pyf:
                if index == 0:
                    pyf.write(f"from .models import {key}")
                else:
                    if index == len(data) - 1:
                        pyf.write(f", {key}\n")
                    else:
                        pyf.write(f", {key}")

            with open(app_basefiles[3], "a", encoding="utf-8") as pyf:
                if index == 0:
                    pyf.write(f"from .models import {key}")
                else:
                    if index == len(data) - 1:
                        pyf.write(f", {key}\n")
                    else:
                        pyf.write(f", {key}")

            with open(app_commandfiles[0], "a", encoding="utf-8") as pyf:
                if index == 0:
                    pyf.write(f"from {app_name}.models import {key}")
                else:
                    if index == len(data) - 1:
                        pyf.write(f", {key}\n")
                    else:
                        pyf.write(f", {key}")

            index += 1

        # --- APP_MODELS.PY --- #
        with open(app_basefiles[0], "r", encoding="utf-8") as pyf:
            lines = pyf.readlines()

        with open(app_basefiles[0], "w", encoding="utf-8") as pyf:
            for line in lines:
                if line.strip("\n") != "#":
                    pyf.write(line)

        # --- CREATE_OBJECT.PY --- #
        with open(app_commandfiles[0], "a", encoding="utf-8") as pyf:
            pyf.write("def create(sensor_type, row):\n")

        # --- ITERATE OVER OBJECTS --- #
        index = 0
        for key, values in data.items():
            key = key.replace("-", "")

            # --- APP_ADMIN.PY --- #
            with open(app_basefiles[1], "a", encoding="utf-8") as pyf:
                pyf.write(f"admin.site.register({key})\n")

            # --- APP_VIEWS.PY --- #
            with open(app_basefiles[3], "a", encoding="utf-8") as pyf:
                if index == 0:
                    pyf.write(f"from .serializers import {key.capitalize()}Serializer")
                else:
                    if index == len(data) - 1:
                        pyf.write(f", {key.capitalize()}Serializer\n")
                    else:
                        pyf.write(f", {key.capitalize()}Serializer")

            # --- APP_SERIALIZERS.PY --- #
            with open(app_basefiles[2], "a", encoding="utf-8") as pyf:
                pyf.write(textwrap.dedent(f"""\
                    class {key.capitalize()}Serializer(serializers.HyperlinkedModelSerializer):
                        class Meta:
                            model = {key}
                            fields = "__all__"
                """))

            # --- APP_URLS.PY --- #
            with open(app_basefiles[4], "a", encoding="utf-8") as pyf:
                if index == 0:
                    pyf.write(f"from .views import {key.capitalize()}ViewSet")
                else:
                    if index == len(data) - 1:
                        pyf.write(f", {key.capitalize()}ViewSet\n")
                    else:
                        pyf.write(f", {key.capitalize()}ViewSet")

            # --- CREATE_OBJECT.PY --- #
            with open(app_commandfiles[0], "a", encoding="utf-8") as pyf:
                pyf.write(textwrap.dedent(f"""\
                #
                    if sensor_type == "{key}":
                        command = {key}.objects.create(
                """))

                subindex = 0
                for value in values:
                    pyf.write(textwrap.dedent(f"""\
                    #
                            {value}=row[{subindex}],
                    """))
                    subindex += 1

                pyf.write(textwrap.dedent("""\
                #
                        )
                """))

            index += 1

        # --- APP_URLS.PY --- #
        with open(app_basefiles[4], "a", encoding="utf-8") as pyf:
            pyf.write("router = routers.DefaultRouter()\n")

        # --- ITERATE OVER OBJECTS --- #
        index = 0
        for key, values in data.items():
            key = key.replace("-", "")

            # --- APP_VIEWS.PY --- #
            with open(app_basefiles[3], "a", encoding="utf-8") as pyf:
                pyf.write(textwrap.dedent(f"""\
                    class {key.capitalize()}ViewSet(viewsets.ModelViewSet):
                        serializer_class = {key.capitalize()}Serializer
                        def get_queryset(self):
                            queryset = {key}.objects.all()
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
                """))

            # --- APP_URLS.PY --- #
            with open(app_basefiles[4], "a", encoding="utf-8") as pyf:
                pyf.write(f"router.register(r'{key}', {key.capitalize()}ViewSet, basename='{key}')\n")

        # --- CREATE_OBJECT.PY --- #
        with open(app_commandfiles[0], "a", encoding="utf-8") as pyf:
            pyf.write(textwrap.dedent("""\
                #
                    return command
            """))

        with open(app_commandfiles[0], "r", encoding="utf-8") as pyf:
            lines = pyf.readlines()

        with open(app_commandfiles[0], "w", encoding="utf-8") as pyf:
            for line in lines:
                if line.strip("\n") != "#":
                    pyf.write(line)

        # --- APP_URLS.PY --- #
        with open(app_basefiles[4], "a", encoding="utf-8") as pyf:
            pyf.write(textwrap.dedent("""\
                urlpatterns = [
                    path('', include(router.urls)),
                ]
            """))

        # --- PROJECT_URLS.PY --- #
        with open(project_filenames[0], "a", encoding="utf-8") as pyf:
            pyf.write(textwrap.dedent(f"""\
                class UserSerializer(serializers.HyperlinkedModelSerializer):
                    class Meta:
                        model = User
                        fields = ['url', 'username', 'email', 'is_staff']
                class UserViewSet(viewsets.ModelViewSet):
                    queryset = User.objects.all()
                    serializer_class = UserSerializer
                router = routers.DefaultRouter()
                router.register(r'users', UserViewSet)
                urlpatterns = [
                    path('admin/', admin.site.urls),
                    path('', include(router.urls)),
                    path('sensor/', include('{app_name}.urls')),
                    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
                ]
            """))

        if os.path.exists(f"{app_name}"):
            for filename in app_basefiles:
                os.replace(filename, f"{app_name}/{filename}")
        else:
            print("Target app folder is missing! Aborting ...")
            for d in [app_basefiles, app_commandfiles, project_filenames]:
                for filename in d:
                    os.remove(filename)

        if os.path.exists(f"{app_name}/management/commands/modules"):
            for filename in app_commandfiles:
                os.replace(filename, f"{app_name}/management/commands/modules/{filename}")
        else:
            print("Target app command folder is missing! Aborting ...")
            for d in [app_basefiles, app_commandfiles, project_filenames]:
                for filename in d:
                    os.remove(filename)

        if os.path.exists(f"{project_name}"):
            for filename in project_filenames:
                os.replace(filename, f"{project_name}/{filename.replace('p_', '')}")
        else:
            print("Target project folder is missing! Aborting ...")
            for d in [app_basefiles, app_commandfiles, project_filenames]:
                for filename in d:
                    os.remove(filename)
