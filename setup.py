#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages
from distutils.core import setup, Extension

C_Module = Extension('MathExt', sources = ['MathExt/math.c'])

setup(
      name='MyDemo',
      version='0.1',
      description='MyDemo',
      author='',
      author_email='',
      url='',
      packages=find_packages(),
      ext_modules= [C_Module],
      test_suite="test")
