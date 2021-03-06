#!/usr/bin/env python

from setuptools import setup

setup(name='curly_carnival',
      version='1.0',
      description='Weighted Node List Exercise',
      author='Joe Julian',
      author_email='me@joejulian.name',
      url='https://github.com/joejulian/curly-carnival',
      package_dir={'curly_carnival': 'src'},
      packages=['curly_carnival'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
     )
