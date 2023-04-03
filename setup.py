from setuptools import find_packages, setup
from typing import List

HYPEN_DOT_E = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n','') for req in requirements ]

        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)
        
    return requirements

setup(

name='flight_fare_prediction',
version='0.1.0',
description='flight fare prediction',
author='Abdullah Ateeq',
author_email='abdullahateeq852@gmail.com',
packages= find_packages(),
license='MIT',
install_requires = get_requirements('requirements.txt')



)
