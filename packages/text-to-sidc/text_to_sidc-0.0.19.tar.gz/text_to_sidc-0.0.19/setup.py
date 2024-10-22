import os
from setuptools import setup, find_packages

version = os.getenv('PACKAGE_VERSION', '0.0.1')

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='text_to_sidc',
    version=version,
    description='A library to convert name of object into sidc code',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Serhii Syrota',
    author_email='ssyrota241@gmail.com',
    url='https://github.com/NorwayPoppy/austrian_python',
    packages=find_packages(),
    package_data={"text_to_sidc": ['patterns_data.csv']},
    classifiers=[],
    python_requires='>=3.10',
    install_requires=required,
)
