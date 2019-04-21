from setuptools import setup, find_packages


setup(
    name='pyuplift',
    version='0.0.3.0',
    author='Artem Kuchumov',
    author_email='kuchumov7@gmail.com',
    url='https://github.com/duketemon/pyuplift',
    license='MIT License',
    description='Uplift modeling implementation',
    keywords=['uplift modeling', 'machine learning', 'true-response-modeling', 'incremental-value-marketing'],
    packages=find_packages(),
    install_requires=["pandas>=0.23.4", "scikit-learn>=0.20.0"],
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
