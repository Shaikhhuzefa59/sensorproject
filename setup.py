from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e.'

def get_requirements(file_path:str)->[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

setup(
    name='Fault Detection',
    version = '0.0.1',
    author = 'Huzaifa Wahed Patel',
    author_mail = 'patilhuzaifa@gmail.com',
    install_requirements = get_requirements('requirements.txt'),
    packages = find_packages()
)

