
# setup.py

from setuptools import setup, find_packages

setup(
    name='isiss',
    version='0.2',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'isiss = isiss.main:main',  # Command to call main() from main.py
        ],
    },
)
