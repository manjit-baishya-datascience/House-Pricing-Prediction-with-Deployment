from setuptools import find_packages, setup
from typing import List

# defining builder
HYPHEN_E_DOT = '-e .'

# installing requirements from file
def get_requirements(file_path:str)->List[str]:
    '''
        This function will return the list of requirements...
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        # skipping builder
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

# project metadata
setup(
    name = 'House Price Prediction',
    version = '1.0',
    author = 'Manjit Baishya',
    author_email = 'manjitbaishya01@gmail.com',
    description = 'House Price Prediction on Pakistan Housing Data of 2023',
    packages = find_packages(),
    include_package_data = True,
    install_requires = get_requirements('requirements.txt')
)