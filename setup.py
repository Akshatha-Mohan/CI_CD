from setuptools import find_packages, setup #automatically find all packages in the application
from typing import List
HYPHEN_E_DOT = '-e .'

#requirements.txt -> triggers setup.py
#function to load packages directly from requirements.txt instead of mentioning one by one
def get_requirements(file_path:str) -> List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

#what application is the project?
#install_requires are the dependencies
setup (name = "mlproject",
       version = "0.0.1",
       author="Krish",
       author_email="krishnaik06@gmail.com",
       packages=find_packages(),
       install_requires=get_requirements("requirements.txt"),)

