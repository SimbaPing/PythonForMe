# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-07 22:02:18
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-07 22:02:50

try:
from setuptools import setup
except ImportError:
from distutils.core import setup
config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}
setup(**config)
