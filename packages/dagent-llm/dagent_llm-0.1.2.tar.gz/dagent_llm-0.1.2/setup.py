# coding = utf-8
# @Time    : 2024-10-18  17:11:02
# @Author  : zhaosheng@nuaa.edu.cn
# @Describe: setup.

import os
from setuptools import setup, find_packages
base_dir = os.path.dirname(os.path.abspath(__file__))


def get_long_description():
    readme_path = os.path.join(base_dir, "README.md")
    with open(readme_path, encoding="utf-8") as readme_file:
        return readme_file.read()


def get_project_version():
    version_path = os.path.join(base_dir, "dagent_llm", "version.py")
    version = {}
    with open(version_path, encoding="utf-8") as fp:
        exec(fp.read(), version)
    return version["__version__"]


def get_requirements(path):
    with open(path, encoding="utf-8") as requirements:
        return [requirement.strip() for requirement in requirements]

install_requires = get_requirements(os.path.join(base_dir, "requirements.txt"))
conversion_requires = get_requirements(
    os.path.join(base_dir, "requirements.conversion.txt")
)


setup(
    name="dagent_llm",
    packages=find_packages(),
    install_requires=[
        # 依赖包，例如 click, requests 等
        "dsqlenv",
        "langchain_core",
        "langchain_openai",
    ],
    author="Zhao Sheng",
    author_email="zhaosheng@nuaa.edu.cn",
    url='https://gitee.com/iint/dagent_llm',
    description="A package for LLM operations.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    version=get_project_version(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            # dagent_llm.cli.main
            'dagent_llm=dagent_llm.cli:main',
        ],
    },
    python_requires='>=3.10',
)
