# coding: utf-8
from setuptools import find_packages, setup

setup(
    name='mktpip',
    version='0.0.1',
    description="mktpip is command-line utility for install python private repository.",
    long_description = 'long_description',
    url="https://www.morakot.it",
    author='Rim Sovankiry',
    author_email="sovankiry@morakot.it",
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    data_files=[
        ('',['favo.png','NEWS.rst'])
    ],
    project_urls ={
           'Documentation': 'http://research-development.gitlab-pages.morakot.it/docs/vb-docs',
           'Source Code': 'https://git.morakot.it/toplevel/mktpip',
           'Bug Tracker': 'https://support.morakot.it/projects/bug?jump=welcome',
           'Feature Suggestion': ['fa fa-question','https://support.morakot.it/projects/new-feature/roadmap'],
           'Realease Note':['fa fa-bullhorn','https://git.morakot.it/toplevel/mktpip/blob/dev/NEWS.rst'],
    },
    # install_requires=Requirement,
    license="Morakot Technology",
    classifiers=[
        "Programming Language :: Python :: 2 :: Only",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        mktpip=mktpip.scripts.cli:cli
    ''',
)