#!/usr/bin/env python
# coding: utf-8


try:
    # python setup.py test
    import multiprocessing
except ImportError:
    pass

import mistune_renderers
from setuptools import setup, Extension


def fread(filepath):
    with open(filepath, 'r') as f:
        return f.read()

setup(
    name='mistune-renderers',
    version=mistune_renderers.__version__,
    url='https://github.com/lepture/mistune-renderers',
    author='Hsiaoming Yang',
    author_email='me@lepture.com',
    description='Renderers for Mistune',
    long_description=fread('README.rst'),
    license='BSD',
    packages=['mistune_renderers'],
    zip_safe=False,
    platforms='any',
    tests_require=['nose'],
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Text Processing :: Markup',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
