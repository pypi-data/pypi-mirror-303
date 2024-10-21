from setuptools import setup, find_packages

setup(
    name="CipheBlockScanner",  # Your package name
    version="0.1.0",  # Package version
    description="Tool for analyzing base64-encoded ciphertext and converting it to hexadecimal and plaintext.",
    long_description=open('README.md').read(),  # Pulls from README.md
    long_description_content_type='text/markdown',  # This ensures markdown rendering on PyPI
    url="https://github.com/DeadmanXXXII/Cipher_block_scanner",  # GitHub repo URL
    author="DeadmanXXXII",  # Your name
    author_email="themadhattersplayground@gmail.com",  # Your email
    license="MIT",  # License type
    packages=find_packages(),  # Automatically finds package folders
    install_requires=[
        # List your dependencies here
        # base64, collections, and argparse are built-in libraries, so they can be omitted
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11.0",  # Specify the minimum Python version
)
