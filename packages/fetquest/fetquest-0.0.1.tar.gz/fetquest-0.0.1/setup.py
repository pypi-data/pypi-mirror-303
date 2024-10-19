from setuptools import setup, find_packages
import setuptools

setuptools.setup(
    name = "fetquest",
    version = "0.0.1",
    author = "Dhinesh Palanisamy",
    author_email = "daps.investment@gmail.com",
    description = "Package to help on Stock Market Visualization and Data",
    packages = find_packages(exclude=['contrib', 'docs', 'tests', 'examples'])

)