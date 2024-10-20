# setup.py

from setuptools import setup, find_packages

setup(
    name="DyPi",  # **IMPORTANT:** This name must be unique on PyPI
    version="0.0.1b1",
    author="Marek Jindrich",
    author_email="imooger@gmail.com",
    description="A simple package for calculating factorial and Fibonacci sequences.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/imooger/DyPi",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.6",
)
setup
