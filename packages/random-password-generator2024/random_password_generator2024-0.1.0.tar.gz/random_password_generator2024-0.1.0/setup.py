
from setuptools import setup, find_packages

setup(
    name="random_password_generator2024",
    version="0.1.0",
    description="A random password generator",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Adam Hernandez",
    author_email="adam@hernandez.ac",
    url="https://github.com/DeusExTaco/RandomPasswordGenerator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
