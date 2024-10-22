#!/usr/bin/env python
"""
Standard python setup.py file
to build     : python setup.py build
to install   : python setup.py install --prefix=<some dir>
to clean     : python setup.py clean
to build doc : python setup.py doc
to run tests : python setup.py test
"""

import os
import setuptools

VERSION = 'v0.0.4'

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='chessdata-pyclient',
    version=VERSION,
    author='Keara Soloway',
    author_email='kls286@cornell.edu',
    description='Python library for interacting with the CHESS metadata service',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/CHESSComputing/chessdata-pyclient',
    packages=['chessdata'],
    package_dir={
        'chessdata': 'chessdata'
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        'requests',
        'pyjwt'
    ]
)
