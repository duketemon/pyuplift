import os
from setuptools import setup

lib_folder = os.path.dirname(os.path.realpath(__file__))
requirements_path = os.path.join(lib_folder, 'requirements.txt')
with open(requirements_path, 'r') as f:
    install_requires = f.read().split('\n')

setup(
    name='pyuplift',
    version='0.0.2.1',
    packages=['pyuplift'],
    url='https://github.com/duketemon/pyuplift',
    license='MIT License',
    author='Artem Kuchumov',
    author_email='kuchumov7@gmail.com',
    description='Uplift modeling implementation',
    keywords=['uplift modeling', 'machine learning'],
    install_requires=install_requires
)
