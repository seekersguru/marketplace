import sys
from setuptools import setup, find_packages



# To install the library, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed.
# Try reading the setuptools documentation:
# http://pypi.python.org/pypi/setuptools

REQUIRES = []

setup(
    name="Wedwise MarketPlace",
    version="1.0.0",
    description="Wedwise",
    author_email="",
    url="",
    keywords=["Swagger", "Wedwise"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Wedwise API
    """
)


