#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
  README = f.read()

requires = [
  'robotframework >= 2.8.7',
  'robotframework-selenium2library >= 1.6.0',
  'selenium >= 2.45.0',
  'Pillow >= 2.2.1',
  ]

test_requires = [
  'nose >= 1.3.0',
  ]

classifiers = [
  'Development Status :: 4 - Beta',
  'Environment :: Web Environment',
  'Intended Audience :: Developers',
  'License :: OSI Approved :: MIT License',
  'Natural Language :: English',
  'Operating System :: OS Independent',
  'Programming Language :: Python',
  'Topic :: Software Development :: Quality Assurance',
  'Topic :: Software Development :: Testing',
]

setup(
  name='RobotS2LScreenshot',
  version='0.1',
  description="Provides additional keywords to augment screenshots capabilities of RobotFramework's Selenium2Library, namely cropping and masking to help with perceptual diff testing.",
  long_description=README,
  classifiers=classifiers,
  platforms=['any'],
  url='https://github.com/canaryhealth/RobotS2LScreenshot',
  license='MIT',
  packages=find_packages(),
  include_package_data=True,
  zip_safe=True,
  test_suite='test',
  install_requires=requires,
  tests_require=test_requires,
)
