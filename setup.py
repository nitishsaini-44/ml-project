from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name="mlproject",
    version="0.1.0",
    description="A machine learning project.",
    author="Nitish Saini",
    author_email="nitishsaini044@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    python_requires=">=3.7",
)