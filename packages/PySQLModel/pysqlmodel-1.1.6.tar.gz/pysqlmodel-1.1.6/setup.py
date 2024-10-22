"""
@Project:PySqlModel
@File:setup.py
@Author:函封封
"""

from setuptools import setup, find_packages

setup(
    name="PySqlModel",
    version="1.1.6",
    author="HanFengFeng",
    author_email="mr_jia_han@qq.com",
    description="简单方便的数据库查询包",
    # 项目主页
    url="https://github.com/NeverStopDreamingWang/pysqlmodel",
    # 你要安装的包，通过 setuptools.find_packages 找到当前目录下有哪些包
    packages=find_packages(),
    python_requires='>=3',
    install_requires=[],
    license="BSD 3-Clause",
    project_urls={
        "github": "https://github.com/NeverStopDreamingWang/pysqlmodel",
        "gitee": "https://gitee.com/NeverStopDreamingWang/pysqlmodel",
    }
)

# python setup.py check
# python setup.py sdist bdist_wheel
# twine upload dist/*