#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : keyusage.py
# Author             : Podalirius (@podalirius_)
# Date created       : 31 Jul 2021

from enum import Enum


class KeyUsage(Enum):
    """
    Key Usage

    See: https://msdn.microsoft.com/en-us/library/mt220501.aspx
    """
    
    # Admin key (pin-reset key)
    AdminKey = 0

    # NGC key attached to a user object (KEY_USAGE_NGC)
    NGC = 0x01

    # Transport key attached to a device object
    STK = 0x02

    # BitLocker recovery key
    BitlockerRecovery = 0x03

    # Unrecognized key usage
    Other = 0x04

    # Fast IDentity Online Key (KEY_USAGE_FIDO)
    FIDO = 0x07

    # File Encryption Key (KEY_USAGE_FEK)
    FEK = 0x08

    # DPAPI Key
    DPAPI = 0x09


