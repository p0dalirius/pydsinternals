#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : KerberosPreAuthenticationType.py
# Author             : Podalirius (@podalirius_)
# Date created       : 8 Oct 2021

from enum import Enum


class KerberosPreAuthenticationType(Enum):
    """
    KerberosPreAuthenticationType

    https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4768
    """

    # Logon without Pre-Authentication.
    NO_PA_LOGON = 0

    # This is a normal type for standard password authentication.
    PA_ENC_TIMESTAMP = 2

    # The ETYPE-INFO pre-authentication type is sent by the KDC in a KRB-ERROR indicating a requirement for additional pre-authentication. It is usually used to notify a client of which key to use for the encryption of an encrypted timestamp for the purposes of sending a PA-ENC-TIMESTAMP pre-authentication value. Never saw this Pre-Authentication Type in Microsoft Active Directory environment.
    PA_ETYPE_INFO = 11

    # Used for Smart Card logon authentication.
    PA_PK_AS_REP_OLD = 15

    # Request sent to KDC in Smart Card authentication scenarios.
    PA_PK_AS_REQ = 16

    # This type should also be used for Smart Card authentication, but in certain Active Directory environments, it is never seen.
    PA_PK_AS_REP = 17

    # The ETYPE-INFO2 pre-authentication type is sent by the KDC in a KRB-ERROR indicating a requirement for additional pre-authentication. It is usually used to notify a client of which key to use for the encryption of an encrypted timestamp for the purposes of sending a PA-ENC-TIMESTAMP pre-authentication value. Never saw this Pre-Authentication Type in Microsoft Active Directory environment.
    PA_ETYPE_INFO2 = 19

    # Used in KDC Referrals tickets.
    PA_SVR_REFERRAL_INFO = 20

    # Logon using Kerberos Armoring (FAST). Supported starting from Windows Server 2012 domain controllers and Windows 8 clients.
    PA_ENCRYPTED_CHALLENGE = 138
