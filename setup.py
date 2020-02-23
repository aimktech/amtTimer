#!/usr/bin/env python
import os
from setuptools import setup, find_packages

PACKAGE_NAME = 'amtTimer'

here = os.path.abspath(os.path.dirname(__file__))

# retrieve long description
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as fh:
    README = fh.read()

# retrieve package version
with open(os.path.join(here, PACKAGE_NAME, '__init__.py')) as fh:
    for line in fh:
        if '__version__' in line:
            VERSION=eval(line.split('=')[1].strip(' \r\n'))
            break

# setup
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description='A simple class to measure code performances.',
    long_description=README,
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='',
    author='aimktech',
    author_email='code@aimechanics.tech',
    url=f'https://github.com/aimktech/{PACKAGE_NAME}',
    license='Apache 2.0',
    packages=find_packages(exclude=["docs", "tests"]),
    package_data={PACKAGE_NAME: ["py.typed"]},
    platforms=["any"],
    zip_safe=False,
)