from setuptools import setup, find_packages

setup(
    name="chain_index",
    version="0.1.4",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    package_data={
        "chain_index": ["data/chains.json"]
    },
    install_requires=[
        "pydantic>=1.8.0",
        "typing-extensions>=3.7.4",
    ],
)
