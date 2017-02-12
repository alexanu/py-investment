from dateutil import parser, tz
from datetime import date, datetime
import pandas as pd

def parse_date(date_to_parse):
    """
    Converts strings or datetime objects to UTC timestamps.

    :param date_to_parse: The date to parse.
    :type date_to_parse: datetime or str or Timestamp
    :return: ``pandas.TimeStamp``
    """

    if isinstance(date_to_parse, date):
        raise TypeError('date must be a datetime object. {} was provided'.format(type(date_to_parse)))
    elif isinstance(date_to_parse, pd.TimeSeries):
        if date_to_parse.tz is None:
             return date_to_parse.tz_localize('UTC')
        else:
            return date_to_parse
    elif isinstance(date_to_parse, datetime):
        return pd.Timestamp(date_to_parse.replace(tzinfo=tz.tzutc()), utc=True)
    elif isinstance(date_to_parse, str):
        return pd.Timestamp(parser.parse(date_to_parse, tzinfo=tz.tzutc()), utc=True)
    else:
        raise TypeError('date_to_parse must be a pandas Timestamp, datetime, or a date string. '
                        '{} was provided'.format(type(date_to_parse)))

def old_parse_date(date_to_parse):
    """
    Keeping this around for now...

    :param date_to_parse:
    :return:
    """
    try:
        parsed_date = parser.parse(date_to_parse, tzinfo=tz.tzutc())
    except ValueError:
        raise ValueError('Unable to parse {} to a date_to_parse, must be a string formatted as a date_to_parse '
                         'or a datetime obj'.format(date_to_parse))
    except TypeError:
        if isinstance(date_to_parse, date):
            raise TypeError('date must be a datetime object. {} was provided'.format(type(date_to_parse)))
        elif isinstance(date_to_parse, datetime):
            parsed_date = date_to_parse.replace(tzinfo=tz.tzutc())
        else:
            raise TypeError('date must be a datetime object. {} was provided'.format(type(date_to_parse)))
    except AttributeError:
        parsed_date = date_to_parse.replace(tzinfo=tz.tzutc())

    return pd.to_datetime(parsed_date, utc=True)