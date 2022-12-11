#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : iconfigset.py
# Author             : Podalirius (@podalirius_)
# Date created       : 1 Aug 2021

from enum import Enum


class MergeRules(Enum):
    """
    MergeRules
    Merge rules for merging config sets.
    """

    # Throw an exception if a merge causes a parameter to be overwritten with a different value in the destination config set.
    ThrowOnConflicts = 0

    # Overwrite destination config set.
    Overwrite = 1

    # Keep existing values of the destination config set intact while performing the merge.
    KeepExisting = 2


class ConfigSetMergeException(Exception):
    """
    ConfigSetMergeException

    Represents exceptions thrown while merging two config sets.
    """

    # Gets the MergeSource config set used during the merge operation.
    MergeSource = None

    # Gets the destination config set used during the merge operation.
    MergeDest = None

    def __init__(self, mergeSource, mergeDest, message:str):
        """
        Initializes a new instance of the ConfigSetMergeException class.

        <param name="mergeSource">The MergeSource config set.</param>
        <param name="mergeDest">The destination config set.</param>
        <param name="message">The exception message.</param>
        <param name="inner">The inner exception.</param>
        """
        self.MergeSource = mergeSource
        self.MergeDest = mergeDest
