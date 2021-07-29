#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : setup.py
# Author             : Podalirius (@podalirius_)
# Date created       : 28 Jul 2021

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='dsinternals',
    version='1.2.1',
    description='',
    url='http://github.com/p0dalirius/pydsinternals',
    author='Podalirius',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email='podalirius@protonmail.com',
    packages=setuptools.find_packages(),
    license='GPL2',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
