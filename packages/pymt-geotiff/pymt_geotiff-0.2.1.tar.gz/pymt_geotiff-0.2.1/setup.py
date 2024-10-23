#! /usr/bin/env python
import os
import sys

from setuptools import Extension, find_packages, setup

entry_points = {
    "pymt.plugins": [
        "GeoTiff=pymt_geotiff.bmi:GeoTiff",
    ]
}


def read(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        return fp.read()


long_description = "\n\n".join(
    [read("README.rst"), read("CREDITS.rst"), read("CHANGES.rst")]
)


setup(
    name="pymt_geotiff",
    author="Mark Piper",
    author_email="mark.piper@colorado.edu",
    description="PyMT plugin for pymt_geotiff",
    long_description=long_description,
    version="0.2.1",
    url="https://github.com/mdpiper/pymt_geotiff",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    keywords=["bmi", "pymt"],
    requires_python=">=3.10",
    install_requires=open("requirements.txt", "r").read().splitlines(),
    packages=find_packages(),
    entry_points=entry_points,
    include_package_data=True,
)
