from setuptools import setup
from pg_resourceloader import VERSION

DIST_NAME = "pg_resourceloader"
__author__ = "baozilaji@gmail.com"

setup(
    name=DIST_NAME,
    version=VERSION,
    description="python game: resourceloader",
    packages=[DIST_NAME],
    author=__author__,
    python_requires='>=3.9',
    install_requires=[
        'pg-environment',
        'pg_objectserialization'
    ],
)
