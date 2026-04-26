from setuptools import find_packages, setup


setup(
	name="house-prices-project",
	version="0.1.0",
	package_dir={"": "."},
	packages=find_packages(where="."),
)