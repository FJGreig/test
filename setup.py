# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 16:23:56 2020

@author: Richard.Fletcher
"""

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
    

setup(main_change
    name="xcm_markov_attribution",
    author="Richard Fletcher",
    author_email="richard.fletcher@xcm-uk.com",
    description="XCM Markov Attribution Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["plotting"]),
    install_requires=['pandas', 'numpy', 'sklearn', 'turbodbc', 'pywin32'],
    use_scm_version={'root':'..', 'relative_to':__file__},
    setup_requires=['setuptools_scm'],
    classifiers=["Programming Language :: Python :: 3",
        "Operating System :: Windows",],
    python_requires='>=3.6',
)