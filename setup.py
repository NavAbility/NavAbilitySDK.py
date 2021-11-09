from setuptools import setup, find_packages
import sys
import os

# not all pip versions support python_requires, used below
if sys.version_info < (3, 0):
    sys.exit(
        """
######################################
# Python 3 is needed #
######################################
"""
    )

setup(
    name="navabilitysdk",
    version=0.01,
    author="NavAbility",
    package_dir={"": "src"},
    include_package_data=True,
    packages=find_packages("src", exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    entry_points={
        "console_scripts": [
            "navability = navability.main:cli",
        ]
    },
    python_requires=">=3.5",
    long_description="NavAbility SDK",
    install_requires=[
        "black==21.9b0",
        "click>=8.0.0,<9",
        "globus_sdk==3.1.0",
    ],
)

# aiohttp            3.7.4.post0
# async-timeout      3.0.1
# attrs              21.2.0
# certifi            2021.5.30
# chardet            4.0.0
# charset-normalizer 2.0.6
# click              8.0.1
# gql                3.0.0a6
# graphql-core       3.1.6
# idna               3.2
# marshmallow        3.14.0
# multidict          5.2.0
# numpy              1.21.4
# pep517             0.11.0
# pip                21.2.4
# pip-tools          6.3.0
# pkg_resources      0.0.0
# requests           2.26.0
# setuptools         58.2.0
# tomli              1.2.1
# typing-extensions  3.10.0.2
# urllib3            1.26.7
# websockets         9.1
# wheel              0.37.0
# yarl               1.7.0a4