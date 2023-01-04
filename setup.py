#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Packaging settings."""
# Copyright (c) 2023 koma <okunoya@path-works.net>
# All rights reserved.

# from __future__ import absolute_import, unicode_literals
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

exec(compile(open('imgdup/version.py', "rb").read(),'imgdup/version.py', 'exec'))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='imgdup',
    version=__version__,
    description='Image Duplicate finder using Image Hash.',
    long_description=long_description,
    url='https://github.com/koma75/imgdup/',
    author='koma',
    author_email='okunoya@path-works.net',
    license='MIT',
    classifiers=[
        # Maturity of the project
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities',
    ],

    keywords='cli',

    packages=find_packages(
        exclude=['dist', 'build', 'contrib', 'docs', 'tests']
        ),

    # add your package requirements
    install_requires=['click>=8,<9', 'imagehash>=4.3.1,<5', 'pillow>=9.3.0,<10'],

    entry_points={
        'console_scripts': [
            'imgdup=imgdup.cli:main',
        ],
    },
)
