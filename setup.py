#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import setuptools

console_scripts = """
[console_scripts]
whyclick=whyclick.cli:cli
"""

setup(
    name='whyclick',
    version='0.0.11',
    packages=['whyclick'],
    description="Cos I don't like to click",
    long_description='',
    url = 'https://github.com/alvations/whyclick',
    install_requires = ['pyderman', 'selenium', 'beautifulsoup4', 'tqdm'],
    license="MIT",
    entry_points=console_scripts,
)
