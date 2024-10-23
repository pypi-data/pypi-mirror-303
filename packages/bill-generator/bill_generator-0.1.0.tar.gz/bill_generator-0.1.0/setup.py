from setuptools import setup, find_packages

setup(
    name='bill_generator',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'start=bill_generator.module:main_function',
        ],
    },
)