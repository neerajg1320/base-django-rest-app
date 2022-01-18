from django.test import TestCase
from django.conf import settings


class SampleTest(TestCase):

    def test_settings_dir(self):
        self.assertEqual(str(settings.BASE_DIR), "/ams")
