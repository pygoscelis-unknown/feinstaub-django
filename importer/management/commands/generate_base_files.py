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
        parser.add_argument('-z', '--ziponly', action="store_true", help="Generate only files for sensor types with monthly zips")

    def handle(self, *args, **kwargs):
        load_dotenv()
        zip_only = kwargs["ziponly"]
        project_name = os.environ.get("DJANGO_PROJECT_NAME")
        app_name = os.environ.get("DJANGO_APP_NAME")

        # --- GET HEADER DATA --- #
        with open("./sensor_csv_header.json", encoding="utf-8") as f:
            data = json.load(f)

        if zip_only:
            # Remove all entries of sensor types that do not have monthly zips
            sensor_types = []
            for key in data:
                sensor_types.append(key)
            with open("./sensor_types-zip.json", encoding="utf-8") as f:
                sensor_types_with_zip = json.load(f)
            sensor_types_to_remove = []
            for s in sensor_types:
                if s not in sensor_types_with_zip:
                    sensor_types_to_remove.append(s)
            for s in sensor_types_to_remove:
                data.pop(s)

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
            with open(app_basefiles[0], "a", encoding="utf-8") as pyf:
                pyf.write(textwrap.dedent(f"""\
                    class {key.upper()}(models.Model):
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
                pyf.write(textwrap.dedent(f"""\
                    #
                        class Meta:
                            verbose_name = "{key.upper()}"
                            verbose_name_plural = "{key.upper()}s"
                """))

            # --- IMPORT MODELS --- #
            with open(app_basefiles[1], "a", encoding="utf-8") as pyf:
                if index == 0:
                    pyf.write(f"from .models import {key.upper()}")
                else:
                    if index == len(data) - 1:
                        pyf.write(f", {key.upper()}\n")
                    else:
                        pyf.write(f", {key.upper()}")

            with open(app_basefiles[2], "a", encoding="utf-8") as pyf:
                if index == 0:
                    pyf.write(f"from .models import {key.upper()}")
                else:
                    if index == len(data) - 1:
                        pyf.write(f", {key.upper()}\n")
                    else:
                        pyf.write(f", {key.upper()}")

            with open(app_basefiles[3], "a", encoding="utf-8") as pyf:
                if index == 0:
                    pyf.write(f"from .models import {key.upper()}")
                else:
                    if index == len(data) - 1:
                        pyf.write(f", {key.upper()}\n")
                    else:
                        pyf.write(f", {key.upper()}")

            with open(app_commandfiles[0], "a", encoding="utf-8") as pyf:
                if index == 0:
                    pyf.write(f"from {app_name}.models import {key.upper()}")
                else:
                    if index == len(data) - 1:
                        pyf.write(f", {key.upper()}\n")
                    else:
                        pyf.write(f", {key.upper()}")

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
            # --- APP_ADMIN.PY --- #
            with open(app_basefiles[1], "a", encoding="utf-8") as pyf:
                pyf.write(f"admin.site.register({key.upper()})\n")

            # --- APP_VIEWS.PY --- #
            with open(app_basefiles[3], "a", encoding="utf-8") as pyf:
                if index == 0:
                    pyf.write(f"from .serializers import {key.upper()}Serializer")
                else:
                    if index == len(data) - 1:
                        pyf.write(f", {key.upper()}Serializer\n")
                    else:
                        pyf.write(f", {key.upper()}Serializer")

            # --- APP_SERIALIZERS.PY --- #
            with open(app_basefiles[2], "a", encoding="utf-8") as pyf:
                pyf.write(textwrap.dedent(f"""\
                    class {key.upper()}Serializer(serializers.HyperlinkedModelSerializer):
                        class Meta:
                            model = {key.upper()}
                            fields = "__all__"
                """))

            # --- APP_URLS.PY --- #
            with open(app_basefiles[4], "a", encoding="utf-8") as pyf:
                if index == 0:
                    pyf.write(f"from .views import {key.upper()}ViewSet")
                else:
                    if index == len(data) - 1:
                        pyf.write(f", {key.upper()}ViewSet\n")
                    else:
                        pyf.write(f", {key.upper()}ViewSet")

            # --- CREATE_OBJECT.PY --- #
            with open(app_commandfiles[0], "a", encoding="utf-8") as pyf:
                pyf.write(textwrap.dedent(f"""\
                #
                    if sensor_type == "{key}":
                        command = {key.upper()}.objects.create(
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
            # --- APP_VIEWS.PY --- #
            with open(app_basefiles[3], "a", encoding="utf-8") as pyf:
                pyf.write(textwrap.dedent(f"""\
                    class {key.upper()}ViewSet(viewsets.ModelViewSet):
                        serializer_class = {key.upper()}Serializer
                        def get_queryset(self):
                            queryset = {key.upper()}.objects
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
                            return "{key.upper()} List"
                """))

            # --- APP_URLS.PY --- #
            with open(app_basefiles[4], "a", encoding="utf-8") as pyf:
                pyf.write(f"router.register(r'{key}', {key.upper()}ViewSet, basename='{key}')\n")

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
