#!/usr/bin/env python
from __future__ import with_statement

import sys
try:
    from setuptools import setup, Extension, Command
except ImportError:
    from distutils.core import setup, Extension, Command
from distutils.command.build_ext import build_ext
from distutils.errors import CCompilerError, DistutilsExecError, \
    DistutilsPlatformError

VERSION = '0.0.1'
DESCRIPTION = "Calculates simple functions and uses Wolfram Alpha for more complicated requests."

CLASSIFIERS = filter(None, map(str.strip,
"""
Development Status :: 1 - Unstable
Intended Audience :: Students
License :: OSI Approved :: BSD License
Programming Language :: Python
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.5
Programming Language :: Python :: Implementation :: CPython
Topic :: Software Development :: Libraries :: Python Modules
""".splitlines()))

setup(
        name="CalCalc",
        version=VERSION,
        description=DESCRIPTION,
        long_description=DESCRIPTION,
        classifiers=CLASSIFIERS,
        author="Parker Fagrelius",
        author_email="parkerf@berkeley.edu",
        url="http://github.com/parfa30/hw_10",
        license="BSD",
        packages=['CalCalc'],
        platforms=['any']
)
