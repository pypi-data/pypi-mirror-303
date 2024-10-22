# setup.py

from setuptools import setup, find_packages

setup(
    name="greeting_module",  # Name of your library
    version="0.1.0",  # Version number
    author="kumar",
    author_email="gangarapukumar99@gmail.com",
    description="A simple greeting module",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

