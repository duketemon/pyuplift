from setuptools import setup


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
    install_requires=["pandas>=0.23.4", "scikit-learn>=0.20.0"]
)
