from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_name:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_name) as file:
        requirements=[req.replace("\n","") for req in file.readlines()]
    
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='Student Performance Indicator',
    version='0.0.1',
    author='Dhiraj',
    author_email='dhiraj.shewa@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)