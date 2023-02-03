from setuptools import find_packages, setup
from app import __version__

setup(
    name='jaffle_shop',
    version=__version__,
    description='jaffle shop package with UDFs',
    author='Lorenzo Rubio',
    packages=find_packages(),
    install_requires=[],
    setup_requires=['wheel'],
)

