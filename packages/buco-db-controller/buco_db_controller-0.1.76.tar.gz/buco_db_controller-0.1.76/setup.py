from setuptools import setup, find_packages

setup(
    name='buco_db_controller',
    version='0.1.76',
    packages=find_packages(),
    install_requires=[
        'PyYAML',
        'RapidFuzz',
        'pymongo',
        'dnspython',
        'Unidecode'
    ],
)
