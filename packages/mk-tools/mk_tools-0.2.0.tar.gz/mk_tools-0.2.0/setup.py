#!/usr/bin/env python3
from typing import List
from setuptools import setup, find_packages
import os
import sys

REQUIREMENTS_FILE: str = 'requirements.txt'


def get_long_description() -> str:
    """Return the long description of the project from README.md."""
    long_description = ''
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.isfile(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as fh:
            long_description = fh.read()
    return long_description


def parse_requirements() -> List[str]:
    """Return list of packages without version information."""
    with open(os.path.join(os.path.dirname(__file__), REQUIREMENTS_FILE)) as f:
        lines = f.read().splitlines()
    # requirements = [line.split('==')[0] for line in lines]
    requirements = [line for line in lines]
    return requirements


setup(
    name='mk_tools',
    version='0.2.0',
    packages=find_packages(),
    install_requires=parse_requirements(),
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
)
