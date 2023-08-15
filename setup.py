# -*- coding: utf-8 -*-
"""setup."""

from setuptools import setup
from setuptools import find_packages


requires = []
with open('requirements.txt', 'w') as _file:
    _file.write('\n'.join(requires))

setup(
    name='mozilla-django-oidc-demo',
    version='0.0.3',
    url='https://github.com/andcolombia/libreria-django-python-auth',
    author='mtoshi',
    author_email='publio.diaz@and.gov.co',
    description='Django oidc  app.',
    packages=find_packages(),
    install_requires=requires,
)
