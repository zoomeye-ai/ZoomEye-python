#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

from zoomeyeai import __version__


DEPENDENCIES = open('requirements.txt', 'r', encoding='utf-8').read().split('\n')
README = open('README.rst', 'r', encoding='utf-8').read()

setup(
    name='zoomeyeai',
    version=__version__,
    description='Python library and command-line tool for ZoomEye (https://www.zoomeye.ai/doc)',
    long_description=README,
    long_description_content_type='text/x-rst',
    author='Zoomeye Team',
    url='https://github.com/zoomeye-ai/zoomeye-python',  #
    packages=['zoomeyeai'],
    entry_points={'console_scripts': ['zoomeyeai=zoomeyeai.cli:main']},
    install_requires=DEPENDENCIES,
    keywords=['security tool', 'zoomeye', 'zoomeyeai', 'command tool'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
