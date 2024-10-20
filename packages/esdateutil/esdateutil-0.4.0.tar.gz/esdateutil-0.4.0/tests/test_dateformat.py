from datetime import datetime, timedelta, timezone

import pytest

from esdateutil import dateformat

def assert_dateformat_eval_equals(parser, given_str, expected_datetime):
    assert parser.parse(given_str) == expected_datetime

def assert_dateformat_parse_exceptions(parser, given_str, expected_exception_list):
    expected_exception = ValueError("Unable to parse date string {}: {}".format(given_str, expected_exception_list))
    with pytest.raises(type(expected_exception)) as e:
        parser.parse(given_str)
    assert e.value.args == expected_exception.args

@pytest.mark.parametrize("given_str,expected_datetime", [
    ("2024",                            datetime(year=2024, month=1, day=1, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)),
    ("2024-04",                         datetime(year=2024, month=4, day=1, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)),
    ("2024-04-11",                      datetime(year=2024, month=4, day=11, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)),
    ("2024-04-11T14",                   datetime(year=2024, month=4, day=11, hour=14, minute=0, second=0, microsecond=0, tzinfo=None)),
    ("2024-04-11T14:02",                datetime(year=2024, month=4, day=11, hour=14, minute=2, second=0, microsecond=0, tzinfo=None)),
    ("2024-04-11T14:02:29",             datetime(year=2024, month=4, day=11, hour=14, minute=2, second=29, microsecond=0, tzinfo=None)),
    ("2024-04-11T14:02:29.123",         datetime(year=2024, month=4, day=11, hour=14, minute=2, second=29, microsecond=123000, tzinfo=None)),
    ("2024-04-11T14:02:29.123456",      datetime(year=2024, month=4, day=11, hour=14, minute=2, second=29, microsecond=123000, tzinfo=None)),
    ("2024-04-11T14:02:29.123456789Z",  datetime(year=2024, month=4, day=11, hour=14, minute=2, second=29, microsecond=123000, tzinfo=timezone.utc)),
    ("2024-04-11T14:02:29.1234+05:30",  datetime(year=2024, month=4, day=11, hour=14, minute=2, second=29, microsecond=123000, tzinfo=timezone(timedelta(hours=5, minutes=30)))),
    ("2024-04-11T14:02:29Z",            datetime(year=2024, month=4, day=11, hour=14, minute=2, second=29, microsecond=0, tzinfo=timezone.utc)),
    ("2024-04-11T14:02-01:00",          datetime(year=2024, month=4, day=11, hour=14, minute=2, second=0, microsecond=0, tzinfo=timezone(timedelta(hours=-1, minutes=0)))),
    ("2024-04-11T14Z",                  datetime(year=2024, month=4, day=11, hour=14, minute=0, second=0, microsecond=0, tzinfo=timezone.utc)),
])
def test_strict_date_optional_time(given_str, expected_datetime):
    parser = dateformat.DateFormat("strict_date_optional_time")
    assert_dateformat_eval_equals(parser, given_str, expected_datetime)

# TODO Test actual special date optional time stuff that wouldn't work in strict
@pytest.mark.parametrize("given_str,expected_datetime", [
    ("2024",                            datetime(year=2024, month=1, day=1, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)),
    ("2024-04",                         datetime(year=2024, month=4, day=1, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)),
    ("2024-04-11",                      datetime(year=2024, month=4, day=11, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)),
    ("2024-04-11T14",                   datetime(year=2024, month=4, day=11, hour=14, minute=0, second=0, microsecond=0, tzinfo=None)),
    ("2024-04-11T14:02",                datetime(year=2024, month=4, day=11, hour=14, minute=2, second=0, microsecond=0, tzinfo=None)),
    ("2024-04-11T14:02:29",             datetime(year=2024, month=4, day=11, hour=14, minute=2, second=29, microsecond=0, tzinfo=None)),
    ("2024-04-11T14:02:29.123",         datetime(year=2024, month=4, day=11, hour=14, minute=2, second=29, microsecond=123000, tzinfo=None)),
    ("2024-04-11T14:02:29.123456",      datetime(year=2024, month=4, day=11, hour=14, minute=2, second=29, microsecond=123000, tzinfo=None)),
    ("2024-04-11T14:02:29.123456789Z",  datetime(year=2024, month=4, day=11, hour=14, minute=2, second=29, microsecond=123000, tzinfo=timezone.utc)),
    ("2024-04-11T14:02:29.1234+05:30",  datetime(year=2024, month=4, day=11, hour=14, minute=2, second=29, microsecond=123000, tzinfo=timezone(timedelta(hours=5, minutes=30)))),
    ("2024-04-11T14:02:29Z",            datetime(year=2024, month=4, day=11, hour=14, minute=2, second=29, microsecond=0, tzinfo=timezone.utc)),
    ("2024-04-11T14:02-01:00",          datetime(year=2024, month=4, day=11, hour=14, minute=2, second=0, microsecond=0, tzinfo=timezone(timedelta(hours=-1, minutes=0)))),
    # Below doesn't work in non-strict date formats, because ES. We test for this in test_date_optional_time_hour_timezone_exception.
    #("2024-04-11T14Z",                  datetime(year=2024, month=4, day=11, hour=14, minute=0, second=0, microsecond=0, tzinfo=timezone.utc)),
])
def test_date_optional_time(given_str, expected_datetime):
    parser = dateformat.DateFormat("date_optional_time")
    assert_dateformat_eval_equals(parser, given_str, expected_datetime)

def test_date_optional_time_hour_timezone_exception():
    parser = dateformat.DateFormat("date_optional_time")
    s = "2024-04-11T14Z"
    es = [ValueError("Elasticsearch has a cool bug where strict_date_optional_time allows a timezone offset after the hour value of a time, but date_optional_time does not. String: {}".format(s))]
    assert_dateformat_parse_exceptions(parser, s, es)

@pytest.mark.parametrize("given_str,expected_datetime", [
    ("2024",                            datetime(year=2024, month=1, day=1, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)),
    ("1726861366756",                   datetime(year=2024, month=9, day=20, hour=20, minute=42, second=46, microsecond=756000, tzinfo=None)),
    # NOTE In Python 3.3, some numbers are scuffed due to floating point nonsense. Below check fails, above check succeeds.
    #("1726861366757",                   datetime(year=2024, month=9, day=20, hour=20, minute=42, second=46, microsecond=757000, tzinfo=None)),
])
def test_default_date_parser(given_str, expected_datetime):
    parser = dateformat.DateFormat()
    assert_dateformat_eval_equals(parser, given_str, expected_datetime)

@pytest.mark.parametrize("given_str,expected_datetime", [
    ("2024-01-24",                            datetime(year=2024, month=1, day=24, hour=0, minute=0, second=0, microsecond=0, tzinfo=timezone.utc)),
])
def test_custom_date_string_parser(given_str, expected_datetime):
    parser = dateformat.DateFormat("%Y-%m-%d", tzinfo=timezone.utc)
    assert_dateformat_eval_equals(parser, given_str, expected_datetime)
