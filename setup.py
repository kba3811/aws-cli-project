#!/usr/bin/env python

from distutils.core import setup

setup(
    name='AWS Secrets Manager CLI',
    version='0.1.0',
    packages=['aws_secrets_manager_cli',],
    install_requires=[
        'boto3==1.9.137',
        'botocore==1.12.137',
        'Click==7.0',
    ],
    entry_points={
        'console_scripts': [
	    'aws_secrets_manager_cli=aws_secrets_manager_cli:main',
        ],
    },
)

