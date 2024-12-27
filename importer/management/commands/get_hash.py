import hashlib
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = """
    Gets hash value of the file
    """

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            type=str,
            help="Path to the file.",
        )

    def handle(self, *args, **kwargs):
        filename = kwargs["file"]
        with open(filename, "rb") as f:
            data = f.read()
            md5_hash = hashlib.md5(data).hexdigest()

        return md5_hash
