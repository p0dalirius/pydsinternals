#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : jet_eventlogginglevel.py
# Author             : Podalirius (@podalirius_)
# Date created       : 31 Jul 2021

from enum import Enum


class EventLoggingLevels(Enum):
    """
    EventLoggingLevels

    Options for EventLoggingLevel.
    """

    # Disable all events.
    Disable = 0

    # Default level. Windows 7 and later.
    Min = 1

    # Low verbosity and lower. Windows 7 and later.
    Low = 25

    # Medium verbosity and lower. Windows 7 and later.
    Medium = 50

    # High verbosity and lower. Windows 7 and later.
    High = 75

    # All events.
    Max = 100
