import hashlib
import os
from feinstaub.settings import BASE_DIR
from django.core.management import call_command
from django.test import TestCase


def get_hash(filename: str):
    with open(filename, "rb") as f:
        data = f.read()
        md5_hash = hashlib.md5(data).hexdigest()

    return md5_hash


class CsvHeaderTest(TestCase):
    def test_command_output(self):
        call_command("get_csv_header", date="2022-12-01")
        csv_header_hash = get_hash(os.path.join(BASE_DIR, "sensor_csv_header.json"))
        test_hash = "c524a14a94b7d9620b586fa10a166b77"

        self.assertEqual(csv_header_hash, test_hash)

        call_command("get_csv_header", date="2024-12-01")
        csv_header_hash = get_hash(os.path.join(BASE_DIR, "sensor_csv_header.json"))
        test_hash = "c524a14a94b7d9620b586fa10a166b77"

        self.assertEqual(csv_header_hash, test_hash)

        call_command("get_csv_header", date="2023-12-01")
        csv_header_hash = get_hash(os.path.join(BASE_DIR, "sensor_csv_header.json"))
        test_hash = "8ab4ca2a98635cbed71b3966fe2fc9cb"

        self.assertEqual(csv_header_hash, test_hash)

        call_command("get_csv_header", date="2023-01-01")
        csv_header_hash = get_hash(os.path.join(BASE_DIR, "sensor_csv_header.json"))
        test_hash = "dcd974d99e0622f57297b6e79cd1d4fb"

        self.assertEqual(csv_header_hash, test_hash)
