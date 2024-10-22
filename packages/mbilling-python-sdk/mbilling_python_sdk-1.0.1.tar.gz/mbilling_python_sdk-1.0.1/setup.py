#!/usr/bin/env python
import os.path
import re

from setuptools import setup

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r"""__version__ = ['"]([0-9.]+)['"]""")


def get_version():
    init = open(os.path.join(ROOT, "mbilling", "__init__.py")).read()
    return VERSION_RE.search(init).group(1)


setup(
    name="mbilling-python-sdk",
    version=get_version(),
    install_requires=["requests"],
    description="Python SDK for MagnusBilling API",
    author="Vertoner",
)
