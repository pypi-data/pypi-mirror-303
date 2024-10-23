#!/usr/bin/env python
from setuptools import setup, find_packages

COMPANY_NAME="LOGYCA"
PACKAGE_NAME = "logyca-ai"
VERSION = "0.2.2"

install_requires = ["pydantic>=2.5","openai>=1.37.1","logyca>=0.1.17","PyMuPDF>=1.23.2","pillow>=9.3.0","pytesseract>=0.3.9","python-docx>=1.1.1","openpyxl>=3.1.3","pandas>=2.1.2","tiktoken>=0.5.1"]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=f'An integration package created by the company {COMPANY_NAME} to interact with ChatGPT and analyze documents, files and other functionality of the OpenAI library.',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    license='MIT License',
    author='Jaime Andres Cardona Carrillo',
    author_email='jacardona@outlook.com',
    url='https://github.com/logyca/python-libraries/tree/main/logyca-ai',
    keywords="artificial-intelligence, machine-learning, deep-learning, chatgpt, nlp, language-models, openai, transformers, neural-networks, ai-tools, mlops, data-science, python, data-analysis, automation",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
        "Topic :: Database",
        "Topic :: Database :: Front-Ends",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development",
        "Typing :: Typed",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=install_requires,
)
