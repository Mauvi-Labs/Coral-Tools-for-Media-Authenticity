from setuptools import setup, find_packages

setup(
    name="media-attestation",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "cryptography>=3.4.7",
    ],
)
