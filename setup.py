#!/usr/bin/python

from setuptools import setup

import os

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(name='bookcommit',
        version='1.0',
        author='Oscar Vilaplana',
        author_email='dev@oscarvilaplana.cat',
        description='Mercurial extension to automatically prepend the current bookmark name to the commit message.',
        long_description=read('README.rst'),
        py_modules=['bookcommit'],
        license='GPLv2',
        zip_safe=True,
        url='http://github.com/grimborg/bookcommit',
        download_url='http://pypi.python.org/pypi/bookcommit',
        keywords='mercurial hg scm',
)
