# setup.py

from setuptools import setup, find_packages

setup(
    name='Globza',
    version='2.0.3',
    license='Proprietary',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Sergei Sychev',
    author_email='sch@triz-ri.com',
    description='Browser to interact with the universal IOF (Internet of Functions) service',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)