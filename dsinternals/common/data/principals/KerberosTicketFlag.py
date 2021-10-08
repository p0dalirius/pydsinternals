#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : KerberosTicketFlag.py
# Author             : Podalirius (@podalirius_)
# Date created       : 8 Oct 2021


from enum import Enum


class KerberosTicketFlag(Enum):
    """
    KerberosTicketFlag

    https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4768
    """

    # No error No errors were found.
    KDC_ERR_NONE  = 0x0

    # Client's entry in KDC database has expired No information.
    KDC_ERR_NAME_EXP  = 0x1

    # Server's entry in KDC database has expired No information.
    KDC_ERR_SERVICE_EXP  = 0x2

    # Requested Kerberos version number not supported No information.
    KDC_ERR_BAD_PVNO  = 0x3

    # Client's key encrypted in old master key No information.
    KDC_ERR_C_OLD_MAST_KVNO  = 0x4

    # Server's key encrypted in old master key No information.
    KDC_ERR_S_OLD_MAST_KVNO  = 0x5

    # Client not found in Kerberos database The username doesn’t exist.
    KDC_ERR_C_PRINCIPAL_UNKNOWN  = 0x6

    # Server not found in Kerberos database This error can occur if the domain controller cannot find the server’s name in Active Directory. This error is similar to KDC_ERR_C_PRINCIPAL_UNKNOWN except that it occurs when the server name cannot be found.
    KDC_ERR_S_PRINCIPAL_UNKNOWN  = 0x7

    # Multiple principal entries in KDC database This error occurs if duplicate principal names exist. Unique principal names are crucial for ensuring mutual authentication. Thus, duplicate principal names are strictly forbidden, even across multiple realms. Without unique principal names, the client has no way of ensuring that the server it is communicating with is the correct one.
    KDC_ERR_PRINCIPAL_NOT_UNIQUE  = 0x8

    # The client or server has a null key (master key) No master key was found for client or server. Usually it means that administrator should reset the password on the account.
    KDC_ERR_NULL_KEY  = 0x9

    # Ticket (TGT) not eligible for postdating This error can occur if a client requests postdating of a Kerberos ticket. Postdating is the act of requesting that a ticket’s start time be set into the future. It also can occur if there is a time difference between the client and the KDC.
    KDC_ERR_CANNOT_POSTDATE  = 0xA

    # Requested start time is later than end time There is a time difference between the KDC and the client.
    KDC_ERR_NEVER_VALID  = 0xB

    # Requested start time is later than end time This error is usually the result of logon restrictions in place on a user’s account. For example workstation restriction, smart card authentication requirement or logon time restriction.
    KDC_ERR_POLICY  = 0xC

    # KDC cannot accommodate requested option Impending expiration of a TGT. The SPN to which the client is attempting to delegate credentials is not in its Allowed-to-delegate-to list
    KDC_ERR_BADOPTION  = 0xD

    # KDC has no support for encryption type In general, this error occurs when the KDC or a client receives a packet that it cannot decrypt.
    KDC_ERR_ETYPE_NOTSUPP  = 0xE

    # KDC has no support for checksum type The KDC, server, or client receives a packet for which it does not have a key of the appropriate encryption type. The result is that the computer is unable to decrypt the ticket.
    KDC_ERR_SUMTYPE_NOSUPP  = 0xF

    # KDC has no support for PADATA type (pre-authentication data) Smart card logon is being attempted and the proper certificate cannot be located. This can happen because the wrong certification authority (CA) is being queried or the proper CA cannot be contacted. It can also happen when a domain controller doesn’t have a certificate installed for smart cards (Domain Controller or Domain Controller Authentication templates). This error code cannot occur in event “4768. A Kerberos authentication ticket (TGT) was requested”. It occurs in “4771. Kerberos pre-authentication failed” event.
    KDC_ERR_PADATA_TYPE_NOSUPP  = 0x10

    # KDC has no support for transited type No information.
    KDC_ERR_TRTYPE_NO_SUPP  = 0x11

    # Client’s credentials have been revoked This might be because of an explicit disabling or because of other restrictions in place on the account. For example: account disabled, expired, or locked out.
    KDC_ERR_CLIENT_REVOKED  = 0x12

    # Credentials for server have been revoked No information.
    KDC_ERR_SERVICE_REVOKED  = 0x13

    # TGT has been revoked Since the remote KDC may change its PKCROSS key while there are PKCROSS tickets still active, it SHOULD cache the old PKCROSS keys until the last issued PKCROSS ticket expires. Otherwise, the remote KDC will respond to a client with a KRB-ERROR message of type KDC_ERR_TGT_REVOKED. See RFC1510 for more details.
    KDC_ERR_TGT_REVOKED  = 0x14

    # Client not yet valid—try again later No information.
    KDC_ERR_CLIENT_NOTYET  = 0x15

    # Server not yet valid—try again later No information.
    KDC_ERR_SERVICE_NOTYET  = 0x16

    # Password has expired—change password to reset The user’s password has expired. This error code cannot occur in event “4768. A Kerberos authentication ticket (TGT) was requested”. It occurs in “4771. Kerberos pre-authentication failed” event.
    KDC_ERR_KEY_EXPIRED  = 0x17

    # Pre-authentication information was invalid The wrong password was provided. This error code cannot occur in event “4768. A Kerberos authentication ticket (TGT) was requested”. It occurs in “4771. Kerberos pre-authentication failed” event.
    KDC_ERR_PREAUTH_FAILED  = 0x18

    # Additional pre-authentication required This error often occurs in UNIX interoperability scenarios. MIT-Kerberos clients do not request pre-authentication when they send a KRB_AS_REQ message. If pre-authentication is required (the default), Windows systems will send this error. Most MIT-Kerberos clients will respond to this error by giving the pre-authentication, in which case the error can be ignored, but some clients might not respond in this way.
    KDC_ERR_PREAUTH_REQUIRED  = 0x19

    # KDC does not know about the requested server No information.
    KDC_ERR_SERVER_NOMATCH  = 0x1A

    # KDC is unavailable No information.
    KDC_ERR_SVC_UNAVAILABLE  = 0x1D

    # Integrity check on decrypted field failed The authenticator was encrypted with something other than the session key. The result is that the client cannot decrypt the resulting message. The modification of the message could be the result of an attack or it could be because of network noise.
    KRB_AP_ERR_BAD_INTEGRITY  = 0x1F

    # The ticket has expired The smaller the value for the “Maximum lifetime for user ticket” Kerberos policy setting, the more likely it is that this error will occur. Because ticket renewal is automatic, you should not have to do anything if you get this message.
    KRB_AP_ERR_TKT_EXPIRED  = 0x20

    # The ticket is not yet valid The ticket presented to the server is not yet valid (in relationship to the server time). The most probable cause is that the clocks on the KDC and the client are not synchronized. If cross-realm Kerberos authentication is being attempted, then you should verify time synchronization between the KDC in the target realm and the KDC in the client realm, as well.
    KRB_AP_ERR_TKT_NYV  = 0x21

    # The request is a replay This error indicates that a specific authenticator showed up twice — the KDC has detected that this session ticket duplicates one that it has already received.
    KRB_AP_ERR_REPEAT  = 0x22

    # The ticket is not for us The server has received a ticket that was meant for a different realm.
    KRB_AP_ERR_NOT_US  = 0x23

    # The ticket and authenticator do not match The KRB_TGS_REQ is being sent to the wrong KDC. There is an account mismatch during protocol transition.
    KRB_AP_ERR_BADMATCH  = 0x24

    # The clock skew is too great This error is logged if a client computer sends a timestamp whose value differs from that of the server’s timestamp by more than the number of minutes found in the “Maximum tolerance for computer clock synchronization” setting in Kerberos policy.
    KRB_AP_ERR_SKEW  = 0x25

    # Network address in network layer header doesn't match address inside ticket Session tickets MAY include the addresses from which they are valid. This error can occur if the address of the computer sending the ticket is different from the valid address in the ticket. A possible cause of this could be an Internet Protocol (IP) address change. Another possible cause is when a ticket is passed through a proxy server or NAT. The client is unaware of the address scheme used by the proxy server, so unless the program caused the client to request a proxy server ticket with the proxy server's source address, the ticket could be invalid.
    KRB_AP_ERR_BADADDR  = 0x26

    # Protocol version numbers don't match (PVNO) When an application receives a KRB_SAFE message, it verifies it. If any error occurs, an error code is reported for use by the application. The message is first checked by verifying that the protocol version and type fields match the current version and KRB_SAFE, respectively. A mismatch generates a KRB_AP_ERR_BADVERSION. See RFC4120 for more details.
    KRB_AP_ERR_BADVERSION  = 0x27

    # Message type is unsupported This message is generated when target server finds that message format is wrong. This applies to KRB_AP_REQ, KRB_SAFE, KRB_PRIV and KRB_CRED messages. This error also generated if use of UDP protocol is being attempted with User-to-User authentication.
    KRB_AP_ERR_MSG_TYPE  = 0x28

    # Message stream modified and checksum didn't match The authentication data was encrypted with the wrong key for the intended server. The authentication data was modified in transit by a hardware or software error, or by an attacker. The client sent the authentication data to the wrong server because incorrect DNS data caused the client to send the request to the wrong server. The client sent the authentication data to the wrong server because DNS data was out-of-date on the client.
    KRB_AP_ERR_MODIFIED  = 0x29

    # Message out of order (possible tampering) This event generates for KRB_SAFE and KRB_PRIV messages if an incorrect sequence number is included, or if a sequence number is expected but not present. See RFC4120 for more details.
    KRB_AP_ERR_BADORDER  = 0x2A

    # Specified version of key is not available This error might be generated on server side during receipt of invalid KRB_AP_REQ message. If the key version indicated by the Ticket in the KRB_AP_REQ is not one the server can use (e.g., it indicates an old key, and the server no longer possesses a copy of the old key), the KRB_AP_ERR_BADKEYVER error is returned.
    KRB_AP_ERR_BADKEYVER  = 0x2C

    # Service key not available This error might be generated on server side during receipt of invalid KRB_AP_REQ message. Because it is possible for the server to be registered in multiple realms, with different keys in each, the realm field in the unencrypted portion of the ticket in the KRB_AP_REQ is used to specify which secret key the server should use to decrypt that ticket. The KRB_AP_ERR_NOKEY error code is returned if the server doesn't have the proper key to decipher the ticket.
    KRB_AP_ERR_NOKEY  = 0x2D

    # Mutual authentication failed No information.
    KRB_AP_ERR_MUT_FAIL  = 0x2E

    # Incorrect message direction No information.
    KRB_AP_ERR_BADDIRECTION  = 0x2F

    # Alternative authentication method required According RFC4120 this error message is obsolete.
    KRB_AP_ERR_METHOD  = 0x30

    # Incorrect sequence number in message No information.
    KRB_AP_ERR_BADSEQ  = 0x31

    # Inappropriate type of checksum in message (checksum may be unsupported) When KDC receives KRB_TGS_REQ message it decrypts it, and after that, the user-supplied checksum in the Authenticator MUST be verified against the contents of the request. The message MUST be rejected either if the checksums do not match (with an error code of KRB_AP_ERR_MODIFIED) or if the checksum is not collision-proof (with an error code of KRB_AP_ERR_INAPP_CKSUM).
    KRB_AP_ERR_INAPP_CKSUM  = 0x32

    # Desired path is unreachable No information.
    KRB_AP_PATH_NOT_ACCEPTED  = 0x33

    # Too much data The size of a ticket is too large to be transmitted reliably via UDP. In a Windows environment, this message is purely informational. A computer running a Windows operating system will automatically try TCP if UDP fails.
    KRB_ERR_RESPONSE_TOO_BIG  = 0x34

    # Generic error Group membership has overloaded the PAC. Multiple recent password changes have not propagated. Crypto subsystem error caused by running out of memory. SPN too long. SPN has too many parts.
    KRB_ERR_GENERIC  = 0x3C

    # Field is too long for this implementation Each request (KRB_KDC_REQ) and response (KRB_KDC_REP or KRB_ERROR) sent over the TCP stream is preceded by the length of the request as 4 octets in network byte order. The high bit of the length is reserved for future expansion and MUST currently be set to zero. If a KDC that does not understand how to interpret a set high bit of the length encoding receives a request with the high order bit of the length set, it MUST return a KRB-ERROR message with the error KRB_ERR_FIELD_TOOLONG and MUST close the TCP stream.
    KRB_ERR_FIELD_TOOLONG  = 0x3D

    # The client trust failed or is not implemented This typically happens when user’s smart-card certificate is revoked or the root Certification Authority that issued the smart card certificate (in a chain) is not trusted by the domain controller.
    KDC_ERR_CLIENT_NOT_TRUSTED  = 0x3E

    # The KDC server trust failed or could not be verified The trustedCertifiers field contains a list of certification authorities trusted by the client, in the case that the client does not possess the KDC's public key certificate. If the KDC has no certificate signed by any of the trustedCertifiers, then it returns an error of type KDC_ERR_KDC_NOT_TRUSTED. See RFC1510 for more details.
    KDC_ERR_KDC_NOT_TRUSTED  = 0x3F

    # The signature is invalid This error is related to PKINIT. If a PKI trust relationship exists, the KDC then verifies the client's signature on AuthPack (TGT request signature). If that fails, the KDC returns an error message of type KDC_ERR_INVALID_SIG.
    KDC_ERR_INVALID_SIG  = 0x40

    # A higher encryption level is needed If the clientPublicValue field is filled in, indicating that the client wishes to use Diffie-Hellman key agreement, then the KDC checks to see that the parameters satisfy its policy. If they do not (e.g., the prime size is insufficient for the expected encryption type), then the KDC sends back an error message of type KDC_ERR_KEY_TOO_WEAK.
    KDC_ERR_KEY_TOO_WEAK  = 0x41

    # User-to-user authorization is required In the case that the client application doesn't know that a service requires user-to-user authentication, and requests and receives a conventional KRB_AP_REP, the client will send the KRB_AP_REP request, and the server will respond with a KRB_ERROR token as described in RFC1964, with a msg-type of KRB_AP_ERR_USER_TO_USER_REQUIRED.
    KRB_AP_ERR_USER_TO_USER_REQUIRED  = 0x42

    # No TGT was presented or available In user-to-user authentication if the service does not possess a ticket granting ticket, it should return the error KRB_AP_ERR_NO_TGT.
    KRB_AP_ERR_NO_TGT  = 0x43

    # Incorrect domain or principal Although this error rarely occurs, it occurs when a client presents a cross-realm TGT to a realm other than the one specified in the TGT. Typically, this results from incorrectly configured DNS.
    KDC_ERR_WRONG_REALM  = 0x44

