#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

NAME = "NumRep"

import re

vre = re.compile(r"Version: ([\d.]+)")
def read_file(fil):
    with open(fil) as f:
        a = f.read()
    return a

def getversion():
    fil = read_file('README.rst')
    ver = vre.search(fil)
    vers = ver.group(1)
    return vers

dct = dict(
    name=NAME,
    version=getversion(),
    description='A module to represent numbers by their place value.',
    long_description=read_file("README.rst"),
    keywords='number representation order place value denomination',
    author='Muhammed Shamil K',
    url = 'https://github.com/necessary129/NumRep',
    author_email='note@noteness.cf',
    license='2-clause Simplified BSD',
    packages=[NAME],
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Environment :: Plugins',
    'Intended Audience :: Customer Service',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.1',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Topic :: Utilities',
    ],
    )
if __name__ == '__main__':
    setup(**dct)