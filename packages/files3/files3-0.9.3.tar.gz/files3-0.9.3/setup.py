#!/usr/bin/env python
# coding:utf-8
import os
import sys
import ctypes
import tempfile
from setuptools import find_packages, setup
from setuptools.command.install import install

# 读取 README.md 文件内容
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='files3',
    version='0.9.3',
    description='(pickle+lz4 based) save Python objects in binary to the file system and manage them.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email='2229066748@qq.com',
    maintainer="Eagle'sBaby",
    maintainer_email='2229066748@qq.com',
    packages=find_packages(),
    license='Apache Licence 2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
    ],
    keywords=['pickle', 'lz4', 'file system', 'file management'],
    python_requires='>=3.10',
    install_requires=[
        "lz4",
        # "lz4>=3.1.1",
    ],
    entry_points={
        'console_scripts': [
            'f3 = files3:cmd_show',
            'f3open = files3:cmd_open',
            'f3assoc = files3:cmd_assoc',
            'f3unassoc = files3:cmd_unassoc',
        ],
    },
    package_data={
        'files3': ['f3.ico'],  # 指定 files3 包内的 f3.ico 文件
    },
)
