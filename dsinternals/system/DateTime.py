#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : DateTime.py
# Author             : Podalirius (@podalirius_)
# Date created       : 28 Jul 2021

import datetime


class DateTime(object):
    """
    Documentation for class DateTime

    https://docs.microsoft.com/en-us/dotnet/api/system.datetime?view=net-5.0
    """

    def __init__(self, ticks: int = 0):
        self.ticks = ticks
        if ticks == 0:
            self.Value = datetime.datetime.now()
        else:
            self.Value = datetime.datetime(1601, 1, 1, 0, 0, 0) + datetime.timedelta(seconds=ticks / 1e7)

    def toUniversalTime(self):
        return self.Value.utcnow()

    def toTicks(self):
        return self.ticks

    def __repr__(self):
        return str(self.Value)
