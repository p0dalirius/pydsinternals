#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : KerberosEncryptionType.py
# Author             : Podalirius (@podalirius_)
# Date created       : 8 Oct 2021

from enum import Enum


class KerberosEncryptionType(Enum):
    """
    KerberosEncryptionType

    https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4768
    """

    # Disabled by default starting from Windows 7 and Windows Server 2008 R2.
    DES_CBC_CRC = 0x1

    # Disabled by default starting from Windows 7 and Windows Server 2008 R2.
    DES_CBC_MD5 = 0x3

    # Supported starting from Windows Server 2008 and Windows Vista.
    AES128_CTS_HMAC_SHA1_96 = 0x11

    # Supported starting from Windows Server 2008 and Windows Vista.
    AES256_CTS_HMAC_SHA1_96 = 0x12

    # Default suite for operating systems before Windows Server 2008 and Windows Vista.
    RC4_HMAC = 0x17

    # Default suite for operating systems before Windows Server 2008 and Windows Vista.
    RC4_HMAC_EXP = 0x18
