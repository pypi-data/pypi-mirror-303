#!/usr/bin/env python
# -*- coding:utf-8 -*-

import setuptools
with open("README.md",  "r", encoding='utf-8') as fh:
    long_description = fh.read()
setuptools.setup(
    name="bdcp",  # 模块名称
    version="1.4.20",  # 当前版本
    author="yiluohan1234",  # 作者
    author_email="XX@qq.com",  # 作者邮箱
    description="A big data competition auxiliary package",  # 模块简介
    long_description=long_description,  # 模块详细介绍
    long_description_content_type="text/markdown",  # 模块详细介绍格式
    # url="https://github.com/wupeiqi/fucker",  # 模块github地址
    packages=setuptools.find_packages(),  # 自动找到项目中导入的模块
    include_package_data=True,  # 确保包含data_files中指定的额外文件
    data_files=[
        ('bdcp/sh/cluster.sh', ['bdcp/sh/cluster.sh']),
        ('bdcp/sh/single.sh', ['bdcp/sh/single.sh']),
    ],
    # 模块相关的元数据
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # 依赖模块
    install_requires=[
        'requests',
        'pandas',
        'paramiko==3.0.0',
        'cryptography==36.0.2',
        'pymysql',
    ],
    python_requires='>=3',
)