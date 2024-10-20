import sys

from datetime import datetime, timedelta, timezone

import pytest

from esdateutil import datemath

# TODO We removed several tests that used a timezone of CET - we need some tests that straddle DST timezones to eval how that works in python. zoneinfo is only added in 3.9. tzdata https://pypi.org/project/tzdata/ is 1st party backwards compat option for testing in 3.3
# ES Datemath Tests: https://github.com/elastic/elasticsearch/blob/main/server/src/test/java/org/elasticsearch/common/time/JavaDateMathParserTests.java

def assert_datemath_eval_equals(given, expected, **kwargs):
    dm = datemath.DateMath(**kwargs)
    assert dm.eval(given) == dm.eval(expected)

def assert_datemath_parse_exceptions(given, expected_exception):
    dm = datemath.DateMath()
    with pytest.raises(type(expected_exception)) as e:
        # Consume generator.
        for _ in dm.parse(given):
            pass
    assert e.value.args == expected_exception.args

@pytest.mark.parametrize("given,expected", [
    ("2014-11-18||+y", "2015-11-18"),
    ("2014-11-18||-2y", "2012-11-18"),

    ("2014-11-18||+3M", "2015-02-18"),
    ("2014-11-18||-M", "2014-10-18"),
    ("2014-11-18||-11M", "2013-12-18"),
    ("2014-01-18||-13M", "2012-12-18"),
    ("2014-11-18||+25M", "2016-12-18"),
    ("2014-11-18||+26M", "2017-01-18"),

    ("2014-11-18||+1w", "2014-11-25"),
    ("2014-11-18||-3w", "2014-10-28"),

    ("2014-11-18||+22d", "2014-12-10"),
    ("2014-11-18||-423d", "2013-09-21"),

    ("2014-11-18T14||+13h", "2014-11-19T03"),
    ("2014-11-18T14||-1h", "2014-11-18T13"),
    ("2014-11-18T14||+13H", "2014-11-19T03"),
    ("2014-11-18T14||-1H", "2014-11-18T13"),

    ("2014-11-18T14:27||+10240m", "2014-11-25T17:07"),
    ("2014-11-18T14:27||-10m", "2014-11-18T14:17"),

    ("2014-11-18T14:27:32||+60s", "2014-11-18T14:28:32"),
    ("2014-11-18T14:27:32||-3600s", "2014-11-18T13:27:32"),
])
def test_basic_math(given, expected):
    assert_datemath_eval_equals(given, expected)

def test_lenient_no_math():
    assert_datemath_eval_equals("2014-05-30T20:21", "2014-05-30T20:21:00.000");

def test_lenient_empty_math():
    assert_datemath_eval_equals("2014-05-30T20:21||", "2014-05-30T20:21:00.000");

@pytest.mark.parametrize("given,expected", [
    ("2014-11-18||+1M-1M", "2014-11-18"),
    ("2014-11-18||+1M-1m", "2014-12-17T23:59"),
    ("2014-11-18||-1m+1M", "2014-12-17T23:59"),
    ("2014-11-18||+1M/M", "2014-12-01"),
    ("2014-11-18||+1M/M+1h", "2014-12-01T01"),
])
def test_multiple_adjustments(given, expected):
    assert_datemath_eval_equals(given, expected)

@pytest.mark.parametrize("given,expected", [
    ("now", "2014-11-18T14:27:32"),
    ("now+M", "2014-12-18T14:27:32"),
    ("now+M", "2014-12-18T14:27:32"),
    ("now-2d", "2014-11-16T14:27:32"),
    ("now/m", "2014-11-18T14:27"),
    ("now/M", "2014-11-01T00:00:00"),
])
def test_now(given, expected):
    now = datetime(2014, 11, 18, 14, 27, 32)
    assert_datemath_eval_equals(given, expected, now_fn=lambda _: now)

@pytest.mark.parametrize("given,expected,units_round", [
    ("now", "2014-11-18T14:27:32", datemath.UNITS_ROUND_UP_MILLIS),
    ("now+M", "2014-12-18T14:27:32", datemath.UNITS_ROUND_UP_MILLIS),
    ("now+M", "2014-12-18T14:27:32", datemath.UNITS_ROUND_UP_MILLIS),
    ("now-2d", "2014-11-16T14:27:32", datemath.UNITS_ROUND_UP_MILLIS),
    ("now/m", "2014-11-18T14:27:59.999000", datemath.UNITS_ROUND_UP_MILLIS),
    ("now/M", "2014-11-30T23:59:59.999000", datemath.UNITS_ROUND_UP_MILLIS),
    ("now/m", "2014-11-18T14:27:59.999", datemath.UNITS_ROUND_UP_MILLIS),
    ("now/M", "2014-11-30T23:59:59.999", datemath.UNITS_ROUND_UP_MILLIS),
])
def test_now_round_up(given, expected, units_round):
    now = datetime(2014, 11, 18, 14, 27, 32)
    assert_datemath_eval_equals(given, expected, units_round=units_round, now_fn=lambda _: now)

def test_now_timezone():
    now = datetime(2014, 11, 18, 14, 27, 32)
    assert_datemath_eval_equals("now/m", "2014-11-18T14:27", now_fn=lambda tz: now.replace(tzinfo=tz), timezone=timezone(timedelta(hours=2)))

@pytest.mark.parametrize("given,expected,timezone", [
    ("2014-11-18", "2014-11-18", None),
    ("2014-11-18T09:20", "2014-11-18T09:20", None),

    ("2014-11-18", "2014-11-17T23:00:00.000Z", timezone(timedelta(hours=1))),
    ("2014-11-18T09:20", "2014-11-18T08:20:00.000Z", timezone(timedelta(hours=1))),
])
def test_implicit_rounding(given, expected, timezone):
    assert_datemath_eval_equals(given, expected, timezone=timezone)



@pytest.mark.parametrize("given,expected,timezone,units_round", [
    ("2014-11-18||/y", "2014-01-01", None, datemath.UNITS_ROUND_DOWN),
    ("2014-11-18||/y", "2014-12-31T23:59:59.999000", None, datemath.UNITS_ROUND_UP_MILLIS),
    ("2014-01-01T00:00:00.001||/y", "2014-01-01T00:00:00.000", None, datemath.UNITS_ROUND_DOWN),

    # rounding should also take into account time zone
    ("2014-11-18||/y", "2013-12-31T23:00:00.000Z", timezone(timedelta(hours=1)), datemath.UNITS_ROUND_DOWN),
    ("2014-11-18||/y", "2014-12-31T22:59:59.999000Z", timezone(timedelta(hours=1)), datemath.UNITS_ROUND_UP_MILLIS),

    ("2014-11-18||/M", "2014-11-01", None, datemath.UNITS_ROUND_DOWN),
    ("2014-11-01||/M", "2014-11-01", None, datemath.UNITS_ROUND_DOWN),
    ("2014-11-01||/M", "2014-11-30T23:59:59.999000", None, datemath.UNITS_ROUND_UP_MILLIS),

    ("2014-11-18||/M", "2014-10-31T23:00:00.000Z", timezone(timedelta(hours=1)), datemath.UNITS_ROUND_DOWN),

    ("2014-11-18T14||/w", "2014-11-17", None, datemath.UNITS_ROUND_DOWN),
    ("2014-11-18T14||/w", "2014-11-23T23:59:59.999000", None, datemath.UNITS_ROUND_UP_MILLIS),
    ("2014-11-17T14||/w", "2014-11-17", None, datemath.UNITS_ROUND_DOWN),
    ("2014-11-19T14||/w", "2014-11-17", None, datemath.UNITS_ROUND_DOWN),
    ("2014-11-20T14||/w", "2014-11-17", None, datemath.UNITS_ROUND_DOWN),
    ("2014-11-21T14||/w", "2014-11-17", None, datemath.UNITS_ROUND_DOWN),
    ("2014-11-22T14||/w", "2014-11-17", None, datemath.UNITS_ROUND_DOWN),
    ("2014-11-23T14||/w", "2014-11-17", None, datemath.UNITS_ROUND_DOWN),
    ("2014-11-18||/w", "2014-11-23T23:59:59.999000", None, datemath.UNITS_ROUND_UP_MILLIS),
    ("2014-11-18||/w", "2014-11-16T23:00:00.000Z", timezone(timedelta(hours=1)), datemath.UNITS_ROUND_DOWN),
    ("2014-11-18||/w", "2014-11-17T01:00:00.000Z", timezone(timedelta(hours=-1)), datemath.UNITS_ROUND_DOWN),
    ("2014-11-18||/w", "2014-11-16T23:00:00.000Z", timezone(timedelta(hours=1)), datemath.UNITS_ROUND_DOWN),
    ("2014-11-18||/w", "2014-11-23T22:59:59.999000Z", timezone(timedelta(hours=1)), datemath.UNITS_ROUND_UP_MILLIS),
    #("2014-07-22||/w", "2014-07-20T22:00:00.000Z", 0, false, ZoneId.of("CET")); # TODO CET with DST straddling. Can use dateutil.tz

    ("2014-11-18T14||/d", "2014-11-18", None, datemath.UNITS_ROUND_DOWN),
    ("2014-11-18T14||/d", "2014-11-18T23:59:59.999000", None, datemath.UNITS_ROUND_UP_MILLIS),
    ("2014-11-18||/d", "2014-11-18", None, datemath.UNITS_ROUND_DOWN),
    ("2014-11-18||/d", "2014-11-18T23:59:59.999000", None, datemath.UNITS_ROUND_UP_MILLIS),

    ("2014-11-18T14:27||/h", "2014-11-18T14", None, datemath.UNITS_ROUND_DOWN),
    ("2014-11-18T14:27||/h", "2014-11-18T14:59:59.999000", None, datemath.UNITS_ROUND_UP_MILLIS),
    ("2014-11-18T14||/H", "2014-11-18T14", None, datemath.UNITS_ROUND_DOWN),
    ("2014-11-18T14||/H", "2014-11-18T14:59:59.999000", None, datemath.UNITS_ROUND_UP_MILLIS),
    ("2014-11-18T14:27||/h", "2014-11-18T14", None, datemath.UNITS_ROUND_DOWN),
    ("2014-11-18T14:27||/h", "2014-11-18T14:59:59.999000", None, datemath.UNITS_ROUND_UP_MILLIS),
    ("2014-11-18T14||/H", "2014-11-18T14", None, datemath.UNITS_ROUND_DOWN),
    ("2014-11-18T14||/H", "2014-11-18T14:59:59.999000", None, datemath.UNITS_ROUND_UP_MILLIS),

    ("2014-11-18T14:27:32||/m", "2014-11-18T14:27", None, datemath.UNITS_ROUND_DOWN),
    ("2014-11-18T14:27:32||/m", "2014-11-18T14:27:59.999000", None, datemath.UNITS_ROUND_UP_MILLIS),
    ("2014-11-18T14:27||/m", "2014-11-18T14:27", None, datemath.UNITS_ROUND_DOWN),
    ("2014-11-18T14:27||/m", "2014-11-18T14:27:59.999000", None, datemath.UNITS_ROUND_UP_MILLIS),

    ("2014-11-18T14:27:32.123||/s", "2014-11-18T14:27:32", None, datemath.UNITS_ROUND_DOWN),
    ("2014-11-18T14:27:32.123||/s", "2014-11-18T14:27:32.999000", None, datemath.UNITS_ROUND_UP_MILLIS),
    ("2014-11-18T14:27:32||/s", "2014-11-18T14:27:32", None, datemath.UNITS_ROUND_DOWN),
    ("2014-11-18T14:27:32||/s", "2014-11-18T14:27:32.999000", None, datemath.UNITS_ROUND_UP_MILLIS),
])
def test_explicit_rounding(given, expected, timezone, units_round):
    assert_datemath_eval_equals(given, expected, timezone=timezone, units_round=units_round)


# Test Exceptions
@pytest.mark.parametrize("given,expected_exception", [
    ("2014-11-18||*5", ValueError("operator * at position 12 in 2014-11-18||*5 not supported. valid operators: +, -, /")),
    ("2014-11-18||/2m", ValueError("unit 2 at position 13 in 2014-11-18||/2m not supported in rounding operation. valid units: {}".format(', '.join(datemath.UNITS_DELTA_DEFAULT.keys())))),
    ("2014-11-18||+2a", ValueError("unit a at position 14 in 2014-11-18||+2a not supported in arithmetic operation. valid units: {}".format(', '.join(datemath.UNITS_DELTA_DEFAULT.keys())))),
    ("2014-11-18||+12", ValueError("truncated input whilst parsing number - expected character at position 15 in 2014-11-18||+12, instead reached end of string")),
    ("2014-11-18||-", ValueError("truncated input whilst parsing number - expected character at position 13 in 2014-11-18||-, instead reached end of string")),
])
def test_illegal_math_format(given, expected_exception):
    assert_datemath_parse_exceptions(given, expected_exception)
