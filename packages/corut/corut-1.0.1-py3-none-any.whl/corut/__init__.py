#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
It is aimed to get rid of repetitive lines of code by integrating tools
that use multiple APIs for FastApi and facilitate repetitive operations.
"""

from importlib import metadata

__copyright__ = 'Copyright 2024 ibrahim CÖRÜT'
metadata = metadata.metadata('corut').json
__title__ = metadata['name']
__summary__ = metadata['summary']
__uri__ = 'https://pypi.org/project/corut'
__version__ = metadata['version']
__author__ = 'ibrahim CÖRÜT'
__email__ = metadata['author_email']
__license__ = metadata['license']
__all__ = (
    '__author__',
    '__copyright__',
    '__email__',
    '__license__',
    '__summary__',
    '__title__',
    '__uri__',
    '__version__',
    
    'shell',
    'vcs',
    
    'contenttypes',
)
