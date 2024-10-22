# setup.py
from setuptools import setup, find_packages

PACKAGE_NAME = 'ambientctl'
VERSION = '1.0.3'
DESCRIPTION = 'Ambient Edge Client Command Line Interface'

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': [
            'ambientctl=ambientctl.main:main',
        ],
    },
    author='Ambient Labs Computing - An Edge Compute Company',
    author_email='jose@ambientlabscomputing.com'
)
