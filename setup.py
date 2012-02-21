#!/usr/bin/python

from setuptools import setup

import os
lines = open(os.path.join(os.path.dirname(__file__), 'README.md')).read().strip().splitlines()

sdesc = lines[0]
ldesc = '\n'.join(lines[1:])

setup(name='bookcommit',
        version='1.0',
        author='Oscar Vilaplana',
        author_email='dev@oscarvilaplana.cat',
        description=sdesc,
        long_description=ldesc,
        py_modules=['bookcommit'],
        license='GPLv2',
        zip_safe=True,
        url='http://github.com/grimborg/bookcommit',
        download_url='http://pypi.python.org/pypi/bookcommit',
        keywords='mercurial hg scm',
)
