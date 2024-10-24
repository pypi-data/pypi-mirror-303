#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/23 18:12
# @Author  : 作者名:张铁君
# @Site    : 
# @File    : setup.py.py
# @Project : auto_test_common
# @Software: PyCharm
from setuptools import setup, find_packages

setup(
    name='jh_auto_test_common_utils',
    version='0.1',
    packages=find_packages(),
    description='A simple example package',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/ztj5451/auto_test',  # GitHub 地址
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)
