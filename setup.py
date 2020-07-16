# coding: utf-8
from setuptools import find_packages, setup

setup(
    name='flask-app',
    version='0.0.1',
    description="flask app sample python package for developer learning.",
    long_description = 'long_description',
    url="https://flask.palletsprojects.com/en/1.1.x/tutorial/",
    author='Houy Narun',
    author_email="houy.narun@gmail.com",
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    data_files=[
        ('',['favo.png','NEWS.rst'])
    ],
    # install_requires=Requirement,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 2 :: Only",
        "Operating System :: OS Independent",
    ]
)