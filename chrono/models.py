from django.db import models
from django.utils.timezone import datetime
from datetime import datetime as normal_datetime


class _ChronoDate(models.Model):
    date = models.DateField(null=True, blank=True, db_index=True, unique=True)

    def __repr__(self):
        return self.date


class _ChronoTime(models.Model):
    time = models.TimeField(null=True, blank=True, db_index=True, unique=True)

    def __repr__(self):
        return self.time


class ChronoDateTimeManager(models.Manager):
    def get_queryset(self):
        return super(ChronoDateTimeManager, self).get_queryset().select_related('chrono_date', 'chrono_time')


class ChronoDateTime(models.Model):
    chrono_date = models.ForeignKey(_ChronoDate, related_name='chrono_date')
    chrono_time = models.ForeignKey(_ChronoTime, related_name='chrono_time')

    objects = ChronoDateTimeManager

    @staticmethod
    def convert_chrono_datetime(datetime_instance):
        date, _ = _ChronoDate.objects.get_or_create(date=datetime_instance.date())
        time, _ = _ChronoTime.objects.get_or_create(time=datetime_instance.time())
        return date, time

    @classmethod
    def get(cls, datetime_value, mask='%Y-%m-%d %H:%M:%S'):
        """
        Get datetime and return one default datetime string
        :mask: By default is %Y-%m-%d %H:%M:%S
        :datetime_value: str, datetime, tz.datetime
        """
        if isinstance(datetime_value, datetime):
            _date, _time = cls.convert_chrono_datetime(datetime_value)
        if isinstance(datetime_value, normal_datetime):
            _date, _time = cls.convert_chrono_datetime(datetime_value)
        if isinstance(datetime_value, str) or isinstance(datetime_value, unicode):
            datetime_value = datetime.strptime(datetime_value, mask)
            _date, _time = cls.convert_chrono_datetime(datetime_value)

        chrono, _ = cls.objects.get_or_create(chrono_date=_date, chrono_time=_time)
        return chrono

    def __repr__(self):
        return "%s" % datetime.combine(self.chrono_date.date, self.chrono_time.time)

    def datetime(self):
        return datetime.combine(self.chrono_date.date, self.chrono_time.time)
