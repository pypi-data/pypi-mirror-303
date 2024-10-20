#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Utilities for handling Elasticsearch date strings and date math in Python.

Copyright (c) 2024, Matthew Murr
License: MIT (see LICENSE for details)
https://git.sr.ht/~murr/esdateutil
"""

# ES Ref: https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html#date-math
# ES Implementation:
# - https://github.com/elastic/elasticsearch/blob/main/server/src/main/java/org/elasticsearch/common/time/DateMathParser.java
# - https://github.com/elastic/elasticsearch/blob/main/server/src/main/java/org/elasticsearch/common/time/JavaDateMathParser.java
# ES Tests: https://github.com/elastic/elasticsearch/blob/main/server/src/test/java/org/elasticsearch/common/time/JavaDateMathParserTests.java

import logging

from datetime import datetime, timedelta
from calendar import monthrange

from . import dateformat

LOG = logging.getLogger(__name__)

def units_delta_months_add(d: datetime, n: int) -> datetime:
    month = d.month + n
    year = d.year + (month-1) // 12
    month = (month % 12) or 12
    return d.replace(year=year, month=month)

UNITS_DELTA_DEFAULT = {
    'y': lambda d, n: d.replace(year=d.year+n),
    'M': lambda d, n: units_delta_months_add(d, n),
    'w': lambda d, n: d + timedelta(days=n*7),
    'd': lambda d, n: d + timedelta(days=n),
    'h': lambda d, n: d + timedelta(hours=n),
    'H': lambda d, n: d + timedelta(hours=n),
    'm': lambda d, n: d + timedelta(minutes=n),
    's': lambda d, n: d + timedelta(seconds=n)
}

UNITS_ROUND_DOWN = {
    'y': lambda d: d.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0),
    'M': lambda d: d.replace(day=1, hour=0, minute=0, second=0, microsecond=0),
    'w': lambda d: (d - timedelta(days=d.weekday())).replace(hour=0, minute=0, second=0, microsecond=0),
    'd': lambda d: d.replace(hour=0, minute=0, second=0, microsecond=0),
    'h': lambda d: d.replace(minute=0, second=0, microsecond=0),
    'H': lambda d: d.replace(minute=0, second=0, microsecond=0),
    'm': lambda d: d.replace(second=0, microsecond=0),
    's': lambda d: d.replace(microsecond=0),
}
UNITS_ROUND_DEFAULT = UNITS_ROUND_DOWN

UNITS_ROUND_UP_MICROS = {
    'y': lambda d: d.replace(month=12, day=monthrange(d.year, 12)[1], hour=23, minute=59, second=59, microsecond=999999),
    'M': lambda d: d.replace(day=monthrange(d.year, d.month)[1], hour=23, minute=59, second=59, microsecond=999999),
    'w': lambda d: (d + timedelta(days=6-d.weekday())).replace(hour=23, minute=59, second=59, microsecond=999999),
    'd': lambda d: d.replace(hour=23, minute=59, second=59, microsecond=999999),
    'h': lambda d: d.replace(minute=59, second=59, microsecond=999999),
    'H': lambda d: d.replace(minute=59, second=59, microsecond=999999),
    'm': lambda d: d.replace(second=59, microsecond=999999),
    's': lambda d: d.replace(microsecond=999999),
}
UNITS_ROUND_UP_MILLIS = {
    'y': lambda d: d.replace(month=12, day=monthrange(d.year, 12)[1], hour=23, minute=59, second=59, microsecond=999000),
    'M': lambda d: d.replace(day=monthrange(d.year, d.month)[1], hour=23, minute=59, second=59, microsecond=999000),
    'w': lambda d: (d + timedelta(days=6-d.weekday())).replace(hour=23, minute=59, second=59, microsecond=999000),
    'd': lambda d: d.replace(hour=23, minute=59, second=59, microsecond=999000),
    'h': lambda d: d.replace(minute=59, second=59, microsecond=999000),
    'H': lambda d: d.replace(minute=59, second=59, microsecond=999000),
    'm': lambda d: d.replace(second=59, microsecond=999000),
    's': lambda d: d.replace(microsecond=999000),
}

class DateMath():
    def __init__(self, timezone=None, separator="||", now_str="now", now_fn=lambda tz: datetime.now(tz), date_fn=dateformat.DateFormat().parse, units_delta: dict=None, units_round: dict=None):
        LOG.debug("Initialising new DateMath instance: timezone=%s, separator=\"%s\", now_fn=%s, date_fn=%s, units_delta=%s, units_round=%s", timezone, separator, now_fn, date_fn, units_delta, units_round)

        self.timezone = timezone

        if not separator:
            raise ValueError("separator is empty or none")
        self.separator = separator

        self.now_str = now_str

        self.now_fn = now_fn
        self.date_fn = date_fn

        if units_delta is not None:
            self.units_delta = units_delta.copy()
        else:
            self.units_delta = UNITS_DELTA_DEFAULT

        if units_round is not None:
            self.units_round = units_round.copy()
        else:
            self.units_round = UNITS_ROUND_DEFAULT

    def next(self, s, pos):
        try:
            c = s[pos]
        except IndexError:
            raise ValueError("truncated input - expected character at position {} in {}, instead reached end of string".format(self,idx, s))
        pos += 1
        #LOG.debug("next({s}) = {c}, {pos}")
        return c, pos

    def _parse_anchor(self, s, pos, s_len):
        start = pos

        if self.now_str:
            now_len = len(self.now_str)
            if s_len - start >= now_len and s[start:now_len] == self.now_str:
                pos += now_len
                LOG.debug("_parse_anchor(%s, %i, %i) : now anchor tok [%i,%i)", s, start, s_len, start, pos)
                date = self.now_fn(self.timezone)
                return date, pos

        idx = s.find(self.separator, start, s_len)
        if idx == -1:
            sep_offset = 0
            pos = s_len
            LOG.debug("_parse_anchor(%s, %i, %i) : no separator string %s", s, start, s_len, self.separator)
        else:
            sep_offset = len(self.separator)
            pos = idx + sep_offset
            LOG.debug("_parse_anchor(%s, %i, %i) : separator tok %s from [%i,%i)", s, start, s_len, self.separator, idx, sep_offset)

        end = pos - sep_offset
        LOG.debug("_parse_anchor(%s, %i, %i) : date anchor tok [%i,%i)", s, start, s_len, start, end)

        date = self.date_fn(s[start:end])

        if date.tzinfo is None and not self.timezone is None:
            LOG.debug("_parse_anchor(%s, %i, %i) : adding missing tzinfo to %s with %s", s, start, s_len, date, self.timezone)
            date = date.replace(tzinfo=self.timezone)

        return date, pos

    def _parse_num(self, s, pos):
        start = pos
        try:
            while s[pos] >= '0' and s[pos] <= '9':
                pos += 1
        except IndexError:
            raise ValueError("truncated input whilst parsing number - expected character at position {} in {}, instead reached end of string".format(pos, s))
        LOG.debug("_parse_num(%s, %i) : num tok [%i,%i)", s, pos, start, pos)
        return s[start:pos], pos

    def _parse_math(self, s, pos, s_len):
        LOG.debug("_parse_math(%s, %i, %i) : parsing math from [%i,%i)", s, pos, s_len, pos, s_len)
        initial_start = pos
        while pos < s_len:
            start = pos
            op, pos = self.next(s, pos)
            if op == '+' or op == '-':
                sign = -1 if op == '-' else 1

                num_s, pos = self._parse_num(s, pos)
                try:
                    num = int(num_s)
                except ValueError:
                    # It is valid to drop the number from arithmetic operations, e.g. +y instead of +1y.
                    # If the unit identifier is invalid, we will throw later in the code.
                    num = 1

                unit, pos = self.next(s, pos)
                try:
                    delta_fn = self.units_delta[unit]
                except KeyError:
                    valid_units = ', '.join(self.units_delta.keys())
                    raise ValueError("unit {} at position {} in {} not supported in arithmetic operation. valid units: {}".format(unit, pos-1, s, valid_units))

                LOG.debug("_parse_math(%s, %i, %i) : delta expr [%i,%i)", s, initial_start, s_len, start, pos)
                yield lambda d: delta_fn(d, sign * num)
            elif op == '/':
                unit, pos = self.next(s, pos)
                try:
                    round_fn = self.units_round[unit]
                except KeyError:
                    valid_units = ', '.join(self.units_round.keys())
                    raise ValueError("unit {} at position {} in {} not supported in rounding operation. valid units: {}".format(unit, pos-1, s, valid_units))
                #print(op, delta)
                LOG.debug("_parse_math(%s, %i, %i) : round expr [%i,%i)", s, initial_start, s_len, start, pos)
                yield round_fn
            else:
                raise ValueError("operator {} at position {} in {} not supported. valid operators: +, -, /".format(op, pos-1, s))

    def parse(self, s, start=0):
        #LOG.debug("parse(%s, %i) : called", s, start)
        pos = start
        s_len = len(s)

        anchor_date, pos = self._parse_anchor(s, pos, s_len)
        yield anchor_date

        if pos < s_len:
            math_fns = self._parse_math(s, pos, s_len)
            yield from math_fns

    def eval(self, s, start=0):
        LOG.debug("eval(%s, %i) : called", s, start)
        it = self.parse(s, start)
        date = next(it)
        for fn in it:
            date = fn(date)

        return date

if __name__ == "__main__":
    from datetime import timezone
    logging.basicConfig(level=logging.DEBUG)
    dm = DateMath(timezone=timezone(timedelta(hours=1)))
    for s in ("2014-11-18||/m+y", "2011-11-04||+1m/d",  "2011-11-04T00:01:11||/d+7d", "2011-11-04"):
        toks = dm.parse(s)
        print(s, next(toks), dm.eval(s))
