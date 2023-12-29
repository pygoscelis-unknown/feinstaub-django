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

    def handle(self, *args, **kwargs):
        path = kwargs['path']

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
                                {} = models.IntegerField(null=True)
                            """).format(value))
                        elif value == "sensor_type":
                            pyf.write(textwrap.dedent("""\
                            #
                                {} = models.CharField(max_length=255, blank=True)
                            """).format(value))
                        elif value == "timestamp":
                            pyf.write(textwrap.dedent("""\
                            #
                                {} = models.DateTimeField(null=True)
                            """).format(value))
                        else:
                            pyf.write(textwrap.dedent("""\
                            #
                                {} = models.FloatField(null=True)
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

            # append content to create_object.py
            for key, values in data.items():
                key = key.replace("-", "")

                with open("create_object.py", "a") as pyf:
                    pyf.write(textwrap.dedent("""\
                        from test_app.models import {}
                    """.format(key)))

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
                        if value == "sensor_id"\
                                or value == "location":
                            pyf.write(textwrap.dedent("""\
                            #
                                    {}=int(row[{}]),
                            """).format(value, index))
                        elif value == "sensor_type":
                            pyf.write(textwrap.dedent("""\
                            #
                                    {}=row[{}],
                            """).format(value, index))
                        elif value == "timestamp":
                            pyf.write(textwrap.dedent("""\
                            #
                                    {}=row[{}],
                            """).format(value, index))
                        else:
                            pyf.write(textwrap.dedent("""\
                            #
                                    {}=float(row[{}]),
                            """).format(value, index))
                        index += 1

                    pyf.write(textwrap.dedent("""\
                    #
                            )
                    """.format(key, key)))

            with open("create_object.py", "a") as pyf:
                pyf.write(textwrap.dedent("""\
                    #
                        return command
                """))
