#!/usr/bin/env python
import os
from setuptools import find_packages, setup

NAME = 'psp'
PACKAGES = [ 'psp' ]
META_PATH = os.path.join('psp', '__init__.py')
KEYWORDS = [ 'color' 'colour' 'terminal' 'text' 'ansi' 'minimalist' ]
CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Terminals',
]

# see classifiers http://pypi.python.org/pypi?%3Aaction=list_classifiers
if __name__ == '__main__':
    setup(
        name=NAME,
        version='0.0.3',
        description='python color printer - minimalist color printing',
        long_description='python simple (color) printing - simple barebones wrappers for 256-color stdout.',
        license='MIT',
        url='https://github.com/someburner/psp',
        author='Jeff Hufford',
        author_email='jeffrey92@gmail.com',
        maintainer='Jeff Hufford',
        keywords=KEYWORDS,
        packages=find_packages('psp'),
        package_dir={'psp': 'psp'},
        classifiers=CLASSIFIERS,
        python_requires='>=3.5',
    )
