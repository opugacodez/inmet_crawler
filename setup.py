from setuptools import setup

NAME = 'inmet_crawler'
VERSION = '0.0.1'
DESCRIPTION = ''
AUTHOR = 'Richard Barros'
EMAIL = 'richardpuga2002@gmail.com'
URL = 'https://github.com/BarrosRichard/inmet_crawler'

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

REQUIRES = [
    'requests'
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    install_requires=REQUIRES,
    classifiers=[
        'Programming Language :: Python :: 3.10.6',
        'License :: Richard Barros',
    ]
)