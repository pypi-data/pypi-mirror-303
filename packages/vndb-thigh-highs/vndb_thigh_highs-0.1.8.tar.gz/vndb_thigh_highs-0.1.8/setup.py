#!/bin/env python

import setuptools

with open("README.md") as readme_file:
    long_description = readme_file.read()

author_email = (
    "example.hello|simple"
    .replace("|", "@")
    .replace("example", "foiegras")
    .replace("simple", "simplelogin.com")
    .replace("hello", "hkx0v")
)

setuptools.setup(
    name="vndb-thigh-highs",
    version="0.1.8",
    author="foiegras",
    author_email=author_email,
    description="VNDB api client implementation and dumps helper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://code.blicky.net/FoieGras/vndb-thigh-highs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
)
