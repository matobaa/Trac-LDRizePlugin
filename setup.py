#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = '0.1'

setup(
    name='LDRize',
    version=version,
    classifiers=['Development Status :: 4 - Beta',
                 'Framework :: Trac'],
    license='Modified BSD',
    author='MATOBA Akihiro',
    author_email='matobaa+trac-hacks@gmail.com',
    url='http://trac-hacks.org/wiki/matobaa',
    description='vi-like keyboard navigation with j or k key',
    zip_safe=True,
    packages=find_packages(exclude=['*.tests']),
    package_data={'ldrize': ['htdocs/**']},
    entry_points={
        'trac.plugins': [
            'LDRize = ldrize.handler',
        ]
    },
)
