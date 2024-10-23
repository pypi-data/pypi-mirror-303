import codecs
import os
from setuptools import setup, find_packages

# these things are needed for the README.md show on pypi (if you dont need delete it)
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# you need to change all these
VERSION = '1.0.7'
DESCRIPTION = 'a gamma simulator '
LONG_DESCRIPTION = 'This is a gamma pulse simulator developed in python that can provide a software foundation for ' \
                   'signal customization in deep learning'

setup(
    name="gamma_simulator",
    version=VERSION,
    author="Chen_zk",
    author_email="",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'urllib3',
    ],
    license='BSD-3-Clause',
    keywords=['python', 'gamma', 'pulse','simulate'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
