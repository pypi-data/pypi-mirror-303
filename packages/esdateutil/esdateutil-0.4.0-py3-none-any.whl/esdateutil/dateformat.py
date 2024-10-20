#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Utilities for handling Elasticsearch date strings and date math in Python.

Copyright (c) 2024, Matthew Murr
License: MIT (see LICENSE for details)
https://git.sr.ht/~murr/esdateutil
"""

# ES Ref: https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-date-format.html
# ES Implementation:
# - https://github.com/elastic/elasticsearch/blob/main/server/src/main/java/org/elasticsearch/common/time/DateFormatter.java
# - https://github.com/elastic/elasticsearch/blob/main/server/src/main/java/org/elasticsearch/common/time/DateFormatters.java
# ES Tests: https://github.com/elastic/elasticsearch/blob/main/server/src/test/java/org/elasticsearch/common/time/DateFormattersTests.java

# TODO For rounding up and down. These need to be funcs to deal with max day of month
#DATETIME_ROUND_DOWN = datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
#DATETIME_ROUND_UP =  datetime(year=1970, month=12, day=31, hour=24, minute=59, second=59, microsecond=999999, tzinfo=None)
#DATETIME_DEFAULT = DATETIME_ROUND_DOWN

import logging
from datetime import datetime, timedelta, timezone

LOG = logging.getLogger(__name__)

DATE_FORMATS = {}
def dateformat_fn(fn):
    DATE_FORMATS[fn.__name__] = fn
    return fn

class DateFormat:
    def __init__(self, fmt=None, separator="||", tzinfo=None):
        """
        Initialises self.

        Takes an optional fmt and separator string.

        fmt can be a string of format strings separated by separator, or a list
        of format strings and/or functions that take a date string, tzinfo, and
        position integer and returns a datetime.

        A format string can be one of the formats defined in
        dateformat.DATE_FORMATS or a Python strptime format string.
        """
        self.fmt_fns = []
        self.fmt_names = []
        self.tzinfo = tzinfo

        if not fmt:
            self.fmt_fns = [strict_date_optional_time, epoch_millis]
            self.fmt_names = ["strict_date_optional_time", "epoch_millis"]
            return

        if type(fmt) is str:
            fmt = fmt.split(separator)

        try:
            for elem in fmt:
                if type(elem) is str:
                    def _custom_format_fn(s, tzinfo, pos):
                        d = datetime.strptime(s, elem)
                        return d if d.tzinfo else d.replace(tzinfo=tzinfo)

                    fn = DATE_FORMATS.get(elem, _custom_format_fn)
                    self.fmt_fns.append(fn)
                    self.fmt_names.append(elem)
                # NOTE We don't know if the given function functions. Sure hope it does :)
                elif callable(elem):
                    self.fmt_fns.append(elem)
                    self.fmt_names.append(elem.__name__)
                else:
                    raise TypeError("Bad type {} of element {}".format(type(elem), elem))
        except TypeError:
            raise TypeError("DateFormat cannot init - expected fmt to be string separated by separator ({}) or list of functions and/or strings. Instead got {}".format(fmt))

    def __repr__(self):
        return "DateFormat({})".format('||'.join(self.fmt_names))

    def parse(self, s, pos=0):
        failed = []
        for fmt_fn in self.fmt_fns:
            try:
                return fmt_fn(s, tzinfo=self.tzinfo, pos=pos)
            except ValueError as e:
                failed.append(e)
        # If we don't return, unable to parse.
        raise ValueError("Unable to parse date string {}: {}".format(s, failed))

def _parse_num(s, strict_len=None, pos=0):
    if strict_len is not None and strict_len <= 0:
        raise ValueError("_parse_num: strict_len must be gte 0 or None. Received {}".format(strict_len))

    start = pos
    s_len = len(s)
    while pos < s_len and s[pos] >= '0' and s[pos] <= '9':
        pos += 1
        if strict_len is not None and strict_len < pos - start:
            raise ValueError("Exceeded strict length when parsing number in {} at [{},{}). Expected strict length of {}".format(s, start, pos, strict_len))
    if strict_len is not None and strict_len > pos - start:
        raise ValueError("Did not meet strict length when parsing number in {} at [{},{}). Expected strict length of {}, got {}".format(s, start, pos, strict_len, pos-start))

    num = int(s[start:pos])
    return num, pos

def _parse_fractional_num(s, fraction_len, pos=0):
    if fraction_len is None or fraction_len <= 0:
        raise ValueError("_parse_fractional_num: fraction_len must be gte 0 or None. Received {}".format(fraction_len))

    start = pos
    s_len = len(s)
    while pos < s_len and s[pos] >= '0' and s[pos] <= '9':
        pos += 1
        if pos - start > 9:
            raise ValueError("Exceeded maximum length (9) of a fractional second when parsing {} at [{},{}).".format(s, start, pos))

    if fraction_len < pos - start:
        end = start + fraction_len
    else:
        end = pos

    num = int(s[start:end]) * (10 ** (end - start))
    return num, pos

def _parse_t_timezone_offset_or_none(s, pos):
    s_len = len(s)
    tz_sign = 0
    if s[pos] == 'Z':
        pos += 1
        if s_len > pos:
            raise ValueError("Parsed timezone offset in {} but unparsed chars remain".format(s))
        return timezone.utc, pos
    elif s[pos] == '+':
        tz_sign = 1
    elif s[pos] == '-':
        tz_sign = -1
    else:
        return None, pos
    pos += 1

    strict_len = 2 # FIXME TZ offset must always be 0 padded, strict does not affect
    tz_hours, pos = _parse_num(s, strict_len, pos)
    if tz_hours < 0 or tz_hours >= 24:
        raise ValueError("Timezone hours must be in [0,24) for string {}, got {}".format(s, tz_hours))
    if s_len <= pos:
        return timezone(tz_sign * timedelta(hours=tz_hours)), pos

    if s[pos] != ':':
        raise ValueError("Invalid character when parsing timezone at position {} in string {}: '{}'".format(pos, s, s[pos]))
    pos += 1

    strict_len = 2
    tz_minutes, pos = _parse_num(s, strict_len, pos)
    if tz_minutes < 0 or tz_hours >= 60:
        raise ValueError("Timezone minutes must be in [0,60) for string {}, got {}".format(s, tz_minutes))
    if s_len <= pos:
        return timezone(tz_sign * timedelta(hours=tz_hours, minutes=tz_minutes)), pos

    # TZ offset must always be at the end of the string.
    raise ValueError("Parsed timezone offset in {} but unparsed chars remain".format(s))

def _parse_date(s, *, strict=False, pos=0):
    strict_len = strict * 4 or None
    year, pos = _parse_num(s, strict_len, pos)
    s_len = len(s)
    if s_len <= pos:
        return year, 1, 1, pos

    if s[pos] != '-':
        raise ValueError("Unparsed characters when parsing date in {} at {}. Expected char '-', got '{}'".format(s, pos, s[pos]))
    pos += 1

    strict_len = strict * 2 or None
    month, pos = _parse_num(s, strict_len, pos)
    if s_len <= pos:
        return year, month, 1, pos

    if s[pos] != '-':
        raise ValueError("Unparsed characters when parsing date in {} at {}. Expected char '-', got '{}'".format(s, pos, s[pos]))
    pos += 1

    strict_len = strict * 2 or None
    day, pos = _parse_num(s, strict_len, pos)

    return year, month, day, pos

def parse_date(s, *, strict=False, tzinfo=None, pos=0):
    year, month, day, pos = _parse_date(s, strict=strict, pos=pos)
    if len(s) == pos:
        return datetime(year, month, day, tzinfo=tzinfo)

    raise ValueError("Unparsed characters when parsing date in {} at {}. Expected end of string, got '{}'".format(s, pos, s[pos]))

# TODO t_time and strict_t_time, time and strict_time, and their no_millis variants
def _parse_t_time(s, *, strict=False, pos=0, fraction_len=3):
    if s[pos] != 'T':
        raise ValueError("t_time must begin with T")
    pos += 1

    strict_len = strict * 2 or None
    hour, pos = _parse_num(s, strict_len, pos)
    s_len = len(s)
    if s_len <= pos:
        return hour, 0, 0, 0, None, pos

    tzinfo, pos = _parse_t_timezone_offset_or_none(s, pos)
    if tzinfo and strict:
        return hour, 0, 0, 0, tzinfo, pos
    elif tzinfo:
        raise ValueError("Elasticsearch has a cool bug where strict_date_optional_time allows a timezone offset after the hour value of a time, but date_optional_time does not. String: {}".format(s))

    if s[pos] != ':':
        raise ValueError("Unparsed characters when parsing time in {} at {}. Expected char ':', got '{}'".format(s, pos, s[pos]))
    pos += 1

    strict_len = strict * 2 or None
    minute, pos = _parse_num(s, strict_len, pos)
    if s_len <= pos:
        return hour, minute, 0, 0, None, pos

    tzinfo, pos = _parse_t_timezone_offset_or_none(s, pos)
    if tzinfo:
        return hour, minute, 0, 0, tzinfo, pos

    if s[pos] != ':':
        raise ValueError("Unparsed characters when parsing time in {} at {}. Expected char ':', got '{}'".format(s, pos, s[pos]))
    pos += 1

    strict_len = strict * 2 or None
    second, pos = _parse_num(s, strict_len, pos)
    if s_len <= pos:
        return hour, minute, second, 0, None, pos

    tzinfo, pos = _parse_t_timezone_offset_or_none(s, pos)
    if tzinfo:
        return hour, minute, second, 0, tzinfo, pos

    # NOTE ES doesn't document this but the behaviour of fractional seconds is
    # to allow any format of them but only take the top N digits when
    # calculating the value.
    if s[pos] != '.':
        raise ValueError("Unparsed characters when parsing time in {} at {}. Expected char '.', got '{}'".format(s, pos, s[pos]))
    pos += 1

    strict_len = None
    micros, pos = _parse_fractional_num(s, fraction_len, pos)
    if s_len <= pos:
        return hour, minute, second, micros, None, pos

    tzinfo, pos = _parse_t_timezone_offset_or_none(s, pos)
    if tzinfo:
        return hour, minute, second, micros, tzinfo, pos

def parse_date_optional_time(s, *, strict=False, tzinfo=None, pos=0, fraction_len=3):
    year, month, day, pos = _parse_date(s, strict=strict, pos=pos)
    s_len = len(s)
    if pos == s_len:
        return datetime(year, month, day)

    hour, minute, second, micros, s_tzinfo, pos = _parse_t_time(s, strict=strict, pos=pos, fraction_len=fraction_len)
    tzinfo = s_tzinfo or tzinfo
    if pos >= s_len:
        return datetime(year, month, day, hour, minute, second, micros, tzinfo=tzinfo)

    raise ValueError("Unparsed characters when parsing date optional time in {} at {}. Expected end of string, got '{}'".format(s, pos, s[pos]))

# Dateformat Named Funcs
@dateformat_fn
def strict_date(s, tzinfo=None, pos=0):
    return parse_date(s, strict=True, tzinfo=tzinfo, pos=pos)

@dateformat_fn
def date(s, tzinfo=None, pos=0):
    return parse_date(s, strict=False, tzinfo=tzinfo, pos=pos)

@dateformat_fn
def strict_date_optional_time(s, *, tzinfo=None, pos=0):
    return parse_date_optional_time(s, strict=True, tzinfo=tzinfo, pos=pos)

@dateformat_fn
def date_optional_time(s, *, tzinfo=None, pos=0):
    return parse_date_optional_time(s, strict=False, tzinfo=tzinfo, pos=pos)

@dateformat_fn
def strict_date_optional_time_nanos(s, *, tzinfo=None, pos=0):
    LOG.warning("As Python has microsecond precision in datetime objects, it can't handle all nanosecond precision timestamps. Therefore, we only handle the first 6 digits of a fractional time in strict_date_optional_time_nanos")
    return parse_date_optional_time(s, strict=True, tzinfo=tzinfo, pos=pos, fraction_len=6)

@dateformat_fn
def epoch_millis(s, *, tzinfo=None, pos=0):
    epoch_s = s[pos:pos+13]
    epoch = int(epoch_s)/1000
    return datetime.fromtimestamp(epoch, tz=tzinfo)

@dateformat_fn
def epoch_second(s, *, tzinfo=None, pos=0):
    epoch_s = s[pos:pos+10]
    epoch = int(epoch_s)
    return datetime.fromtimestamp(epoch, tz=tzinfo)

if __name__ == "__main__":
    print(DATE_FORMATS)
    parser = None
    for strict in True, False:
        parser = DateFormat("{}date_optional_time".format('strict_' if strict else ''))
        print("Parser:", parser)
        for s in ["2024", "2024-04", "2024-04-11", "2024-04-11T14", "2024-04-11T14:02", "2024-04-11T14:02:29", "2024-04-11T14:02:29.123", "2024-04-11T14:02:29.123456", "2024-04-11T14:02:29.123456789Z",  "2024-04-11T14:02:29.1234+05:30", "2024-04-11T14:02:29Z", "2024-04-11T14:02+01:00",  "2024-04-11T14Z"]:
            print(s)
            #print(parse_date_optional_time(s, strict=strict))
            print(parser.parse(s))
