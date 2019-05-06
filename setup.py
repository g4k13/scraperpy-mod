# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='scraperpy-pygdev',
    version='0.0.1',
    description='News Scraper',
    long_description=readme,
    scripts=['pyg-scraperpy'],
    author='g4k13',
    author_email='g4k13@github.com',
    url='https://github.com/g4k13/scraperpy-mod',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

