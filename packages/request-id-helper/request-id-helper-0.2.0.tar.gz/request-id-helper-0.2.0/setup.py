#!/usr/bin/env python
import pathlib
from importlib.machinery import SourceFileLoader

from setuptools import find_packages, setup

version = SourceFileLoader("version", "request_id_helper/version.py").load_module()


_ROOT = pathlib.Path(__file__).parent

with open(str(_ROOT / "README.md")) as f:
    readme = f.read()

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Operating System :: POSIX",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Environment :: Console",
    "Intended Audience :: Developers",
]

setup(
    name="request-id-helper",
    version=str(version.VERSION),
    license="Apache License, Version 2.0",
    description="Helper to add request id in logger and context",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Pavel Liashkov",
    author_email="pavel.liashkov@protonmail.com",
    maintainer="Pavel Liashkov",
    maintainer_email="pavel.liashkov@protonmail.com",
    download_url="https://pypi.python.org/pypi/request-id-helper",
    url="https://github.com/bigbag/request-id-helper",
    platforms=["POSIX"],
    classifiers=CLASSIFIERS,
    python_requires=">=3.7",
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite="",
)
