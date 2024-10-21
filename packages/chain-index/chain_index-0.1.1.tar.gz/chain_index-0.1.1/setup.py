from setuptools import setup, find_packages

setup(
    name="chain_index",
    version="0.1.0",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "pydantic>=1.8.0",
        "typing-extensions>=3.7.4",
    ],
)
