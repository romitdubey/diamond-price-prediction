from setuptools import setup, find_packages
from typing import List

def getrequirement(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if '-e.' in requirements:
            requirements.remove('-e.')
        return requirements


setup(
    name='Diamond Price Prediction',
    author= 'Romit Dubey',
    author_email='romitdubey1@gmail.com',
    install_requires = getrequirement('requirements.txt'),
    packages= find_packages()
)