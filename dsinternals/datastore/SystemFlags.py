#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : SystemFlags.py
# Author             : Podalirius (@podalirius_)
# Date created       : 31 Jul 2021

from enum import Enum


class SystemFlags(Enum):
	"""
	SystemFlags

	An integer value that contains flags that define additional properties of the class.

	https://msdn.microsoft.com/en-us/library/ms680022(VS.85).aspx
	"""

	# When applied to an attribute, the attribute will not be replicated.
	# When applied to a Cross-Ref object, the naming context is in NTDS.
	DO_NOT_REPLICATE = 1 # (0x00000001)

	# When applied to an attribute, the attribute will be replicated to the global catalog.
	# When applied to a Cross-Ref object, the naming context is a domain.
	REPLICATE_ATTRIBUTE = 2 # (0x00000002)

	# When applied to an attribute, the attribute is constructed.
	CONSTRUCT_ATTRIBUTE = 4 # (0x00000004)

	# When set, indicates the object is a category 1 object. A category 1 object is a class or attribute that is
	# included in the base schema included with the system.
	CATEGORY_1_OBJECT = 16 # (0x00000010)

	# The object is not moved to the Deleted Objects container when it is deleted. It will be deleted immediately.
	DELETE_IMMEDIATELY = 33554432 # (0x02000000)

	# The object cannot be moved.
	CANNOT_BE_MOVED = 67108864 # (0x04000000)

	# The object cannot be renamed.
	CANNOT_BE_RENAMED = 134217728 # (0x08000000)

	# For objects in the configuration partition, if this flag is set, the object can be moved with restrictions; otherwise,
	# the object cannot be moved. By default, this flag is not set on new objects created under the configuration partition.
	# This flag can only be set during object creation.
	CAN_BE_MOVED_RESTRICTED = 268435456 # (0x10000000)

	# For objects in the configuration partition, if this flag is set, the object can be moved; otherwise, the object cannot
	# be moved. By default, this flag is not set on new objects created under the configuration partition. This flag can only
	# be set during object creation.
	CONFIGURATION_CAN_BE_MOVED = 536870912 # (0x20000000)

	# For objects in the configuration partition, if this flag is set, the object can be renamed; otherwise, the object cannot
	# be renamed. By default, this flag is not set on new objects created under the configuration partition. This flag can only
	# be set during object creation.
	CAN_BE_RENAMED = 1073741824 # (0x40000000)

	# The object cannot be deleted.
	CANNOT_BE_DELETED = 2147483648 # (0x80000000)

