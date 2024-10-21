from setuptools import setup
from pg_mysql import VERSION

DIST_NAME = "pg_mysql"
__author__ = "baozilaji@gmail.com"

setup(
    name=DIST_NAME,
    version=VERSION,
    description="python game: mysql",
    packages=[DIST_NAME],
    author=__author__,
    python_requires='>=3.9',
    install_requires=[
        'pg-environment>=0',
        'SQLAlchemy==1.4.27',
        'python-dateutil==2.8.2',
        'aiomysql==0.1.1',
    ],
)
