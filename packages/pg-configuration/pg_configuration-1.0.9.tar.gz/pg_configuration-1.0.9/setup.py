from setuptools import setup
from pg_configuration import VERSION

DIST_NAME = "pg_configuration"
__author__ = "baozilaji@gmail.com"

setup(
    name=DIST_NAME,
    version=VERSION,
    description="python game: configuration",
    packages=[DIST_NAME],
    author=__author__,
    python_requires='>=3.9',
    install_requires=[
        'pg-environment>=0',
        'openpyxl==3.1.2'
    ],
)
