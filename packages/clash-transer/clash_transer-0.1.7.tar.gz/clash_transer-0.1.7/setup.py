#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs

import setuptools
import setuptools.command.test


def long_description():
    try:
        return codecs.open("README.md", "r", "utf-8").read()
    except IOError:
        return "Long description error: Missing README.md file"


setuptools.setup(
    name="clash_transer",
    packages=setuptools.find_packages(),
    version="0.1.7",
    description="机场订阅转换工具",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    keywords="clash_transer",
    author="TT",
    author_email="123@mail.com",
    license="BSD",
    platforms=["Linux"],
    install_requires=["requests", "PyYAML", "funcy", "Brotli"],
    python_requires=">=3.10.4",
    # extras_require=extras_require(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": ["mct = clash_transer:main"],
    },
    url="",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: POSIX :: Linux",
    ],
)
