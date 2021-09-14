from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in fx/__init__.py
from fx import __version__ as version

setup(
	name="fx",
	version=version,
	description="FX",
	author="SERVIO Technologies",
	author_email="janguluan@servio.ph",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
