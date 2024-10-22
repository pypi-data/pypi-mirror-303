from setuptools import setup, find_packages

setup(
    name='cysteine_counter',
    version='1.2',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'cysteine_counter': ['data/*.json', 'data/*.txt'],
    }
)

