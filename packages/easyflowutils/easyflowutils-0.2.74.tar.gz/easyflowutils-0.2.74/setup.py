from setuptools import setup, find_packages

setup(
    name='easyflowutils',
    version="0.2.74",
    author='Nadav Friedman',
    author_email='info@easyflow.co.il',
    description='A utility package for Easy Flow automation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://easyflow.co.il/',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
    install_requires=[
        'requests',
        'pydantic',
        'phonenumbers',
        'flask'
    ],
)
