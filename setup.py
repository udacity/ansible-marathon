#!/usr/bin/env python

from distutils.core import setup

setup(
    name='ansible-marathon',
    version='0.2.0',
    description=' An Ansible module for deploying applications to Mesos through Marathon',
    url='https://github.com/udacity/ansible-marathon',
    py_modules=[
        'ansible_marathon.marathon',
    ],
    author='James Earl Douglas',
    author_email='james@earldouglas.com',
)
