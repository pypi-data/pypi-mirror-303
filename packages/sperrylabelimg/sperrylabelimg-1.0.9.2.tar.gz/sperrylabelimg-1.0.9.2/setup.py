"""
setup
"""
from setuptools import setup, find_packages


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='sperrylabelimg',
    version='1.0.9.2',
    description='A GUI for labelling images customized for usage at Sperry Rail',
    author='Brooklyn Germa',
    author_email='brooklyn.germa@sperryrail.com',
    url='https://gitlab.com/bGerma/customlabelimg',
    license='MIT',
    packages=find_packages(),
    package_data={
        "sperryLabelImg": ["resources/*", "sperryLabelImg/*"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=required,
    entry_points='''
        [console_scripts]
        sperrylabelimg=sperryLabelImg.app:main
    ''',
)
