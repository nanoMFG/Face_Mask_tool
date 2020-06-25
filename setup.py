import os
from setuptools import find_packages, setup

with open(os.path.join('.', 'VERSION')) as version_file:
    version = version_file.read().strip()

setup(
    name='RENAME',
    version=version,
    long_description=open('README.md').read(),
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    include_package_data=True,
)