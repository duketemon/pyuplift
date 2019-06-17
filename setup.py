import os
import codecs
from setuptools import setup, find_packages

path = os.path.abspath(os.path.dirname(__file__))


def read(filename):
    return codecs.open(os.path.join(path, filename), 'r').read()


setup(
    name='pyuplift',
    version='0.0.4.0',
    license='MIT License',
    author='Artem Kuchumov',
    author_email='kuchumov7@gmail.com',
    url='https://github.com/duketemon/pyuplift',
    description='Uplift modeling implementation',
    long_description=read('README.MD'),
    long_description_content_type='text/markdown',
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(),
    keywords=['uplift modeling', 'machine learning', 'true response modeling', 'incremental value marketing'],
    install_requires=[
        'pandas>=0.23.4',
        'scikit-learn>=0.20.0',
        'requests>=2.19.1',
    ],
    extras_require={
        'tests': [
            'pytest>=4.5.0'
        ]
    },
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
