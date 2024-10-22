# -*- coding: utf-8 -*-
#############################################
# File Name: setup.py
# Author: Yixin Li
# Mail: 20185414@stu.neu.edu.cn
# Created Time:  2021-12-11
#############################################
from setuptools import setup, find_packages



with open("README.md", 'r', encoding='utf-8') as f:
    readme = f.read()


setup(
    name="deepcad",
    version="1.3.0",
    description=("Implement DeepCAD-RT to denoise data by "
                 "removing independent noise"),
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Xinyang Li, Yixin Li",
    author_email="liyixin318@gmail.com",
    url="https://github.com/cabooster/DeepCAD-RT",
    license="GNU General Public License v2.0",
    packages=find_packages(),
    install_requires=['matplotlib','pyyaml','tifffile','scikit-image','opencv-python','csbdeep','gdown==4.2.0'],
)
