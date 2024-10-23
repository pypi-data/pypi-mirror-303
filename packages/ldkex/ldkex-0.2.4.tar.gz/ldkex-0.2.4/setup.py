import os
from setuptools import setup, find_packages

version = os.getenv('PACKAGE_VERSION', '0.0.1')

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='ldkex',
    version=version,
    description='A library to read .ldk files without color loss',
    long_description=open('readme.md').read(),
    long_description_content_type='text/markdown',
    author='Adam Wood',
    author_email='adamwoodintel@gmail.com',
    url='https://github.com/adamwoodintel/ldkex',
    packages=find_packages(),
    classifiers=[],
    python_requires='>=3.11',
    install_requires=required,
)
