# (c) 2017 Continuum Analytics, Inc. / http://continuum.io
# All Rights Reserved
from setuptools import setup
import sys

from conda_verify import __version__

if sys.version_info.major == 2:
    requirements = ['backports-functools-lru-cache']
else:
    requirements = []


setup(
    name="conda-verify",
    version=__version__,
    author="Continuum Analytics, Inc.",
    author_email="conda@continuum.io",
    url="https://github.com/conda/conda-verify",
    license="BSD",
    description="A tool for validating conda recipes and conda packages",
    long_description=open('README.md').read(),
    packages=['conda_verify'],
    install_requires=requirements,
    entry_points='''
        [console_scripts]
        conda-verify=conda_verify.cli:cli
        ''',
)
