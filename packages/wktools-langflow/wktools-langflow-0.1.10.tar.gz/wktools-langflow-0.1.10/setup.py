# setup.py
from setuptools import setup, find_packages

setup(
    name="wktools-langflow",
    version="0.1.10",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],  # Add any dependencies here
    description="A tools for langflow",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/kokhou/jwtools",
    author="kokhou",
    author_email="kokhou.choi@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
