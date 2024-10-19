from setuptools import find_packages, setup
from setuptools.config.expand import entry_points

setup(
    name='ranver_transaction_counter_1',
    description='summarise finantial data1',
    version='0.2.1',
    py_modules=['transaction_counter'],
    entry_points={
        'console_scripts': [
            'transaction_counter = transaction_counter:main'
        ]
    },
)