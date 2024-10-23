# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:22:51 2024

@author: 91600
"""


  
from setuptools import setup, find_packages

setup(
    name="credit_pdfextract",            # 包名
    version="0.2",                # 版本号
    description="a pdf extract library",  # 简短描述
    author="Cheng kang",           # 作者名
    packages=find_packages(),
    install_requires=['pdfplumber','pandas'],    # 自动查找模块
)

