#!/usr/bin/env python
# coding:utf-8
import os
import sys
import ctypes
import tempfile
from setuptools import find_packages, setup
from setuptools.command.install import install



setup(
    name='reft',
    version='0.3.6',
    description='re format-tool (FT FDict Flist Fset...) and a simple mono-like control language (Support QMonoWidget QMonoInspector if PyQt5 is installed, but not neccessary if not used)',
    author_email='2229066748@qq.com',
    maintainer="Eagle'sBaby",
    maintainer_email='2229066748@qq.com',
    packages=find_packages(),
    license='Apache Licence 2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
    ],
    keywords=['re'],
    python_requires='>=3.10',
    install_requires=[
    ],
)
