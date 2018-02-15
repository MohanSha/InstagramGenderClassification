from setuptools import setup

__version__ = '0.0.1'
__author__ = 'Mohan Sha'

requirements = [
    'selenium',
    'requests'
]

description = 'Training data generation for InstaPy sex classification'

setup(
    name='instapy_sex_class',
    version=__version__,
    author=__author__,
    author_email='mohansha@outlook.com',
    url='https://github.com/MohanSha/InstagramGenderClassification',
    py_modules='instapy_class',
    description=description,
    install_requires=requirements
)