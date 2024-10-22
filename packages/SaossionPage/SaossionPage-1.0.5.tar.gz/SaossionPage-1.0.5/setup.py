import codecs
import os

from setuptools import find_packages, setup

# these things are needed for the README.md show on pypi
# 获取当前文件所在的目录，即项目的根目录
here = os.path.abspath(os.path.dirname(__file__))

# 打开并读取 README.md 文件，使用 utf-8 编码
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    # 将读取的内容作为包的详细描述，并在前面添加一个空行
    long_description = "\n" + fh.read()



VERSION = '1.0.5'
DESCRIPTION = 'A sao shen library'
LONG_DESCRIPTION = 'The brother version of the Drissionpage library, SaossionPage, is referred to as Sao Shen for short.'

# Setting up
# 使用 setuptools 中的 setup 函数来配置包
setup(
    # 包的名称
    name="SaossionPage",

    # 包的版本号
    version=VERSION,
    # 包的作者
    author="sao shen",
    # 包的作者邮箱
    author_email="",
    # 包的简短描述
    description=DESCRIPTION,
    # 长描述的内容类型
    long_description_content_type="text/markdown",
    # 包的详细描述，从 README.md 文件中读取
    long_description=long_description,
    # 是否包含包中的非 Python 文件
    include_package_data=True,
    # 自动发现和包含所有的包和子包
    packages=find_packages(),
    # 安装这个包所需的依赖项
    # zip_safe=False,
    install_requires=[
        'DrissionPage',
        'colorama',
        
    ],
    # 一些关键词，用于帮助用户在 PyPI 上搜索到这个包
    keywords=['python', 'menu', 'saoshen', 'windows', 'SaossionPage', 'linux'],
    # 一些分类信息，用于描述包的开发状态、适用的受众、编程语言和操作系统等
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)


# 1 修改完善 setup.py
# 2 进行本地测试 python setup.py develop
# 3 编译 python setup.py sdist
# 4 上传到pypi twine upload dist/*
