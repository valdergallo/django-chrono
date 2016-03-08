from django.test import TestCase
from chrono.models import ChronoDateTime
from datetime import datetime


class TestChronoDateField(TestCase):

    def test_create_datetime(self):
        date_time = ChronoDateTime.get('2014-01-31 14:12', mask='%Y-%m-%d %H:%M')
        self.assertEqual(date_time.to_datetime(), datetime(2014, 01, 31, 14, 12, 00))

    def test_not_duplicate_datetime(self):
        ChronoDateTime.get('2014-01-31 14:12', mask='%Y-%m-%d %H:%M')
        ChronoDateTime.get('2014-01-31 14:12', mask='%Y-%m-%d %H:%M')

        self.assertEqual(ChronoDateTime.objects.count(), 1)

    def test_update_set_mask(self):
        ChronoDateTime.get('2014-01-31', mask='%Y-%m-%d')
        self.assertEqual(ChronoDateTime.objects.count(), 1)

    def test_default_mask(self):
        ChronoDateTime.get('2014-01-31 14:12:12')
        self.assertEqual(ChronoDateTime.objects.count(), 1)

    def test_find_date(self):
        ChronoDateTime.get('2014-01-31 14:12:12')
        self.assertEqual(ChronoDateTime.objects.filter(chrono_date__date='2014-01-31').count(), 1)
