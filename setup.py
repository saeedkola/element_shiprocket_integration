# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in element_shiprocket_integration/__init__.py
from element_shiprocket_integration import __version__ as version

setup(
	name='element_shiprocket_integration',
	version=version,
	description='Create Shiprocket Order Via ERPNext',
	author='Element Labs',
	author_email='saeed@elementlabs.xyz',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
