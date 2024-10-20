#!/usr/bin/env python
# coding:utf-8
import os
import sys
import ctypes
import tempfile
from setuptools import find_packages, setup
from setuptools.command.install import install

setup(
    name='qwork',
    version='0.0.5',
    description='...',
    author_email='2229066748@qq.com',
    maintainer="Eagle'sBaby",
    maintainer_email='2229066748@qq.com',
    packages=find_packages(),
    license='Apache Licence 2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
    ],
    keywords=['pyqt'],
    python_requires='>=3',
    install_requires=[
        "pyqt5>=5.15",
        "files3>=0.9",
    ],
    # entry_points={
    #     'console_scripts': [
    #         'f3 = files3:cmd_show',
    #         'f3open = files3:cmd_open',
    #         'f3assoc = files3:cmd_assoc',
    #         'f3unassoc = files3:cmd_unassoc',
    #     ],
    # },
    # cmdclass={
    #     'install': PostInstallCommand,
    # },
)
