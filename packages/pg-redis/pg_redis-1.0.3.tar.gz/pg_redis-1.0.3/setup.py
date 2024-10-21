from setuptools import setup
from pg_redis import VERSION

DIST_NAME = "pg_redis"
__author__ = "baozilaji@gmail.com"

setup(
    name=DIST_NAME,
    version=VERSION,
    description="python game: redis",
    packages=[DIST_NAME],
    author=__author__,
    python_requires='>=3.9',
    install_requires=[
        'pg-environment>=0',
        'redis==4.6.0',
    ],
)
