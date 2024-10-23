"""
setup
"""
from setuptools import setup, find_packages


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='sperrylabelimg',
    version='1.0.9.6',
    description='A GUI for labelling images customized for usage at Sperry Rail',
    author='Brooklyn Germa',
    author_email='brooklyn.germa@sperryrail.com',
    url='https://gitlab.com/bGerma/customlabelimg',
    license='MIT',
    packages=find_packages(),
    package_data={
        "sperryLabelImg": ["../resources/*"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    password="the hat in the cat in the hat",
    install_requires=required,
    entry_points='''
        [console_scripts]
        sperrylabelimg=app:main
    ''',
)
