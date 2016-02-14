#!/usr/bin/env python3
import re

from setuptools import find_packages, setup
from pip.req import parse_requirements

def read_tags(filename):
    """ Read tags from file
    :param filename:    Filename
    :return: Tags assoc
    """
    tags = {}

    def parse_line(line):
        """ Parse line
        :param line:    Line string
        :return:
        """
        match = re.match("^__(\w*)__\s*=\s*\"(.*)\"", line)
        if match:
            tags[match.group(1)] = match.group(2)

    # Iterate over every line in file
    with open(filename, "r") as file:
        for line in file:
            parse_line(line)

    # Return parsed tags
    return tags

# App constants
PROJECT = "pipm"
APP_EXEC = "pipm"

# List of packages
install_packages = [
    str(ir.req) for ir in parse_requirements("requirements.txt", session=False)
]

# Basic setup info
tags = read_tags(PROJECT + "/__init__.py")

# Installer
setup(
      name=tags['appname']
    , version=tags['version']
    , packages=find_packages(exclude=['tests'])

    , install_requires=install_packages
    , url="https://github.com/pipm/pipm"
    , license=tags['license']

    , author=tags['authors']
    , author_email="cziken58@gmail.com"

    , description=tags['description']
    # , long_description=open("README.rst").read()
    , zip_safe=False
    , entry_points={
        "console_scripts": ["{0}={0}.__main__:main".format(APP_EXEC)]
    }
    , platforms="linux"
    , keywords=["pip", "pipm", "wrapper", "npm"]
    , package_data={
        "pipm": ["requirements.txt"]
    }
    , include_package_data=True
    , classifiers=[
          "Development Status :: 2 - Pre-Alpha"
        , "Intended Audience :: Developers"
        , "Intended Audience :: Information Technology"
        , "Programming Language :: Python"
        , "Programming Language :: Python :: 3"
        , "Programming Language :: Python :: 3.3"
        , "Programming Language :: Python :: 3.4"
    ]
)
