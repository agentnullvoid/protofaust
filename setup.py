#!/usr/bin/env python

from os.path import abspath, dirname, exists, join
from setuptools import setup, find_packages
import sys

base_package = 'protofaust'
base_package_dir = 'src'

setup_dir = abspath(dirname(__file__))
version_file = abspath(join(setup_dir, base_package_dir, base_package, 'version.py'))
requirements_file = abspath(join(setup_dir, 'requirements.txt'))

if not exists(version_file):
    with open(version_file, 'w') as fp:
        fp.write("__version__ = '999.999.999'\n")

with open(version_file, 'r') as fp:
    exec(fp.read(), globals())

with open(join(setup_dir, 'requirements.txt')) as fp:
    install_requires = fp.readlines()

setup(name='protofaust',
      version=__version__,
      description='Faust record generator from Protobuf models',
      author='Alberto De la Rosa Algarin',
      author_email='alberto@uniformzero.io',
      url='https://github.com/agentnullvoid/protofaust',
      package_dir={'': base_package_dir},
      packages=find_packages(base_package_dir),
      install_requires=install_requires,
      entry_points={
        'console_scripts': [
            'protofaust = protofaust.cli:main',
        ]
      }
)
