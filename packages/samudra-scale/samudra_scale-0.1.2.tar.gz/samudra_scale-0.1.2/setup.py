# setup.py

from setuptools import setup, find_packages

setup(
    name="samudra_scale",
    version="0.1.2",
    packages=find_packages(),
    description="A python library for extracting weights from byte data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dap23/samudra-scale",
    author="Muhammad Daffa",
    author_email="mdaffa2301@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
