#!/usr/bin/env python

from setuptools import setup
from pathlib import Path


readme_content = open(Path(__file__).parent.joinpath("README.md"), "r").read()

setup(
    name="appear",
    version="1.2.2",
    description="Make program internals appear in the browser",
    author="Andrew Houghton",
    author_email="houghtonandrew0@gmail.com",
    url="https://github.com/andrew-houghton/appear",
    packages=["appear"],
    package_data={"appear": ["static/*"]},
    include_package_data=True,
    install_requires=["Flask-SocketIO", "grequests"],
    long_description=readme_content,
    long_description_content_type="text/markdown",
)
