from setuptools import setup, find_packages
from typing import List 

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return all of the requirements. 
    """

    requirements_list: List[str] = []

    try:
        # Open and read the requirements.txt file
        with open('requirements.txt', 'r') as file:
            # Read lines from the file 
            lines = file.readlines()
            for line in lines:
                # Strip whitespace and ignore empty lines
                requirement = line.strip()
                if requirement and requirement!='-e .':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found.')
    
    return requirements_list

print(get_requirements('requirements.txt'))
setup(
    name='AI-TRIP-PLANNER',
    version='0.1.0',
    author='Mehedi Hasan',
    author_email='mehedi.43889@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)