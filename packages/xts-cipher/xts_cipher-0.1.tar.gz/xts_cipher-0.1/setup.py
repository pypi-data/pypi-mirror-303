from setuptools import setup, find_packages

setup(
    name="xts_cipher", 
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy", 
    ],
    author="Krunal Chandrakant Dalvi",
    description="A Python package for XTS (XOR-Transposition-Substitution) cipher encryption and decryption",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
