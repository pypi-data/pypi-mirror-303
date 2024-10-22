# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="hshmeng",
    version="2024.10.22.3",
    author="hshmeng",
    author_email="hshmeng@foxmail.com",
    description='猛写的汉化',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=find_packages(where="hshmeng_jet"),  # 指定源代码文件夹
    python_requires=">=3.8",
    license="MIT",
)
