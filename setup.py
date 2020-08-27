# Copyright 2020 The spartan2 Authors.
#
#

import setuptools
from setuptools.extension import Extension
from Cython.Build import cythonize

NAME = 'spartan2'
VERSION = '0.0.2'
DESCRIPTION = 'collection of data mining algorithms on big graphs and time series'
URL = 'https://github.com/BGT-M/spartan2'
AUTHOR = 'Shenghua Liu, Houquan Zhou, Quan Ding, Jiabao Zhang, Xin Zhao, Siwei Zeng,etc'
EMAIL = 'liu.shengh@foxmail.com'

# Get the long description from the README file
with open('README.md', encoding='utf-8') as fp:
    _LONG_DESCRIPTION = fp.read()

extensions = [
    Extension(
        "spartan.model.summarize.c_MDL",
        ["spartan/model/summarize/c_MDL.pyx"],
    ),
]

REQUIRED_PACKAGES = [
    'numpy',
    'scipy',
    'networkx',
    'matplotlib',
    'statsmodels',
    'pomegranate',
    'scikit-learn',
    'scikit-image',
    'sparse',
    'ipdb',
]

setuptools.setup(name=NAME,
                 version=VERSION,
                 description=DESCRIPTION,
                 long_description=_LONG_DESCRIPTION,
                 long_description_content_type='text/markdown',
                 author=AUTHOR,
                 author_email=EMAIL,
                 url=URL,
                 install_requires=REQUIRED_PACKAGES,
                 packages=setuptools.find_packages(),
                 ext_modules=cythonize(extensions),
                 classifiers=[
                     "Programming Language :: Python :: 3",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                 ],
                 python_requires='>=3.6',
                 )
