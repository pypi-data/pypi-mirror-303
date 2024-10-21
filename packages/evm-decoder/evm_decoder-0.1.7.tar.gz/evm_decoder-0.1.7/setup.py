from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="evm-decoder",
    version="0.1.7",
    author="gmatrixuniverse",
    author_email="gmatrixuniverse@gmail.com",
    description="A package for decoding and analyzing EVM transactions and logs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gmatrixuniverse/evm-decoder",
    packages=find_packages(include=['evm_decoder', 'evm_decoder.*']),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        "web3>=5.0.0,<6.0.0",
        "eth-abi>=2.0.0,<3.0.0",
    ],
    include_package_data=True,
    package_data={
        "evm_decoder": ["config/*.json"],
    },
)