# -*- coding: utf-8 -*-
"""setuptools control."""

import re

from setuptools import setup


def get_version():
    """Return __version__ value from main source file."""
    with open("wordstats/__init__.py") as source:
        version = re.search(r"^__version__\s*=\s*'(.*)'",
                            source.read(),
                            re.M).group(1)
    return version


def get_description():
    """Return long description from README."""
    with open("README.rst", "rb") as readme:
        long_description = readme.read().decode("utf-8")
    return long_description


setup(
    name="wordstats",
    packages=["wordstats"],
    test_suite="tests",
    entry_points={
        "console_scripts": [
            "wordstats = wordstats.__main__:main"
        ]
    },
    version=get_version(),
    description="Tool that prints various statistics on the word list",
    long_description=get_description(),
    long_description_content_type="text/x-rst",
    author="Egor Artemov",
    author_email="egor.artemov@gmail.com",
    license="WTFPL",
    url="https://github.com/souryogurt/wordstats",
    install_requires=[],
    setup_requires=[]
)
