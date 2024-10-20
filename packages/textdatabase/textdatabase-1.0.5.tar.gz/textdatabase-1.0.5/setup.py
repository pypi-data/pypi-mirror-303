from setuptools import setup,find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name="textdatabase",  # 模块名称
    version="1.0.5",  # 当前版本
    author="GQX",  # 作者
    author_email="kill114514251@outlook.com",  # 作者邮箱
    description="A little text database for developers",  # 模块简介
    long_description=long_description,  # 模块详细介绍
    long_description_content_type="text/markdown",  # 模块详细介绍格式
    url="https://github.com/BinaryGuo/Bullet_Roulette",  # 模块github地址
    packages=find_packages(),  # 自动找到项目中导入的模块
    package_data={
        "tdb/" : ["tdb","intros/*"]
    },
    # 模块相关的元数据
    classifiers=[
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3"
    ],
    # 依赖模块
    install_requires=[
        "pyotp>=2.6.0",
    ],
    python_requires=">=3"
)