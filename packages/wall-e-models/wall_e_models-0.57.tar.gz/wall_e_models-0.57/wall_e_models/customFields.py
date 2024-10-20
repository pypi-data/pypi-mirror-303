import datetime
import re

import pytz
from dateutil.tz import tz, tzfile
from django.db import models
from django.conf import settings

ENV = getattr(settings, "ENVIRONMENT", "LOCALHOST")

try:
    # necessary if this is being called from wall_e and therefore the settings need to be picked up from
    # django_settings instead of the settings file in the wall_e_models repo
    import django_settings

    ENV = getattr(django_settings, "ENVIRONMENT", "LOCALHOST")
except ModuleNotFoundError:
    pass


class GeneratedIdentityField(models.AutoField):
    description = "An Integer column which uses `GENERATED {ALWAYS | BY DEFAULT} AS IDENTITY`. \
                  A modern alternative to `BIGSERIAL` from the SQL standard."

    def __init__(self, *args, **kwargs):
        # this is necessary because of the `always` that was used in the fourth migrationf
        kwargs.pop('always', None)

        # have to do it like this cause otherwise loaddata will not work when loading datat from PROD,
        # you wind up with the error
        # DETAIL:  Column "ban_id" is an identity column defined as GENERATED ALWAYS.
        # HINT:  Use OVERRIDING SYSTEM VALUE to override.
        self.always = ENV == "PRODUCTION"

        super(GeneratedIdentityField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['always'] = self.always
        return name, path, args, kwargs

    def db_type(self, connection):
        return "INTEGER"


class pstdatetime(datetime.datetime):
    """
    Create a pstdatetime object representing current object
    pstdatetime.now()

    Converting datetime.datetime to pstdatetime
    if the numbers in the datetime.datetime object are already in pacific time
    pstdatetime.from_datetime_with_pst_time(datetime_object)

    if the numbers in the datetime.datetime object are in UTC time
    pstdatetime.from_utc_datetime(datetime_object)

    creating object from epoch time
    pstdatetime.from_epoch(datetime_object)
    """

    PACIFIC_TZ = tz.gettz('Canada/Pacific')
    UTC_TZ = pytz.UTC

    @property
    def pst(self):
        return self.astimezone(self.PACIFIC_TZ) if self.tzinfo == self.UTC_TZ else self

    @property
    def utc(self):
        return self if self.tzinfo == self.UTC_TZ else self.astimezone(self.UTC_TZ)

    @classmethod
    def now(cls, tz=None):
        return super(pstdatetime, cls).now(tz=cls.PACIFIC_TZ)

    @classmethod
    def from_utc_datetime(cls, date: datetime.datetime):
        return pstdatetime(
            date.year, month=date.month, day=date.day, hour=date.hour, minute=date.minute, second=date.second,
            microsecond=date.microsecond, tzinfo=cls.UTC_TZ
        )

    @classmethod
    def from_datetime_with_pst_time(cls, datetime_obj):
        """
        Creates a PST timezone object using a datetime object

        Keyword Arguments
        datetime_obj -- the datetime with the day and time to use to create the PST timezone object

        Return
        datetime -- the PST timezone object
        """
        return pstdatetime(
            year=datetime_obj.year, month=datetime_obj.month, day=datetime_obj.day, hour=datetime_obj.hour,
            minute=datetime_obj.minute, second=datetime_obj.second, tzinfo=cls.PACIFIC_TZ
        )

    @classmethod
    def from_epoch(cls, epoch_time: int):
        try:
            date = pstdatetime.fromtimestamp(epoch_time).astimezone(cls.UTC_TZ)
        except ValueError:
            date = pstdatetime.fromtimestamp(
                int(epoch_time) // 1000
            ).replace(microsecond=int(epoch_time) % 1000 * 10).astimezone(cls.UTC_TZ)
        return date.pst

    @classmethod
    def create_pst_time(cls, year, month, day, hour_24=0, minute=0, second=0):
        """
        Creates a PST timezone object with the given parameters

        Keyword Arguments
        year -- the year (YYYY)
        month -- the month (01-12)
        day -- the day (01-XX)
        hour_24 -- -the hour (0-23)
        minute -- the minute (0-59)
        second -- the second (0-59)

        Return
        datetime -- the PST timezone object
        """
        return pstdatetime(
            year=year, month=month, day=day, hour=hour_24, minute=minute, second=second, tzinfo=cls.PACIFIC_TZ
        )

    @classmethod
    def create_utc_time(cls, year, month, day, hour_24=0, minute=0, second=0):
        """
        Creates a UTC timezone object with the given parameters

        Keyword Arguments
        year -- the year (YYYY)
        month -- the month (01-12)
        day -- the day (01-XX)
        hour_24 -- -the hour (0-23)
        minute -- the minute (0-59)
        second -- the second (0-59)

        Return
        datetime -- the UTC timezone object
        """
        return cls.create_pst_time(
            year=year, month=month, day=day, hour_24=hour_24, minute=minute, second=second
        ).utc


def isfloat(num):
    try:
        float(num)
        return True
    except (ValueError, TypeError):
        return False


class PSTDateTimeField(models.DateTimeField):

    def pre_save(self, model_instance, add):
        """
        Makes sure to convert the date to UTC time before saving if its in Canada/Pacific timezone
        """
        date = getattr(model_instance, self.attname)
        # date can be None cause of end date
        if type(date) == str and date.strip() == "":
            setattr(model_instance, self.attname, None)
        elif f"{date}".isdigit() or (date and isfloat(date)):
            date = pstdatetime.from_epoch(date)
            setattr(model_instance, self.attname, date.utc)
        elif date is not None:
            if type(date) is str and re.match(r"\d{4}-\d{2}-\d{2}", date):
                year = int(date[:4])
                month = int(date[5:7])
                day = int(date[8:10])
                setattr(model_instance, self.attname, pstdatetime.create_utc_time(year, month, day))
            elif date.tzinfo == tzfile('/usr/share/zoneinfo/Canada/Pacific'):
                setattr(model_instance, self.attname, date.utc)
            elif date.tzinfo is None:
                raise Exception("no timezone detected")
        return super(PSTDateTimeField, self).pre_save(model_instance, add)

    def from_db_value(self, value, expression, connection):
        """
        Converts the value from the DB from UTC time to PST time before returning to calling code
        """
        # date can be None cause of end date
        if value is None:
            return None
        return pstdatetime.from_utc_datetime(value).pst
