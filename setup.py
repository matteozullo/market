from setuptools import setup, find_packages

setup(
    name="market",  # Package name
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pandas',  # For data manipulation
    ],
    author="Matteo Zullo",
    description="A package for calculating market concentration indexes",
    url="https://github.com/matteozullo/market",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
