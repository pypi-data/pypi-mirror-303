# -*- coding: utf-8 -*-
"""
@File     : setup.py
@Author   : chengming
@Email    : chengming0412@gmail.com
@Date     : 2024/10/22 17:13
@Blog     : https://blog.chengmingfun.com
@Copyright: © 2024 Your Company. All rights reserved.
"""
from setuptools import setup, find_packages

def parse_requirements(filename):
    """ 从 requirements.txt 中读取依赖库并返回一个列表 """
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='FlexiSpiderTools',
    version='0.1.6',
    author='chengming',
    author_email='863493479@qq.com',
    description='一个用于爬虫的工具包',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=parse_requirements('requirements.txt'),
)
