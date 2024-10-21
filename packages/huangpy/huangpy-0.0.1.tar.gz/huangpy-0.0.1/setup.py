from pathlib import Path
import pkg_resources
from setuptools import find_packages, setup

setup(
    name="huangpy",
    version="0.0.1",
    description="support tool",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    readme="README.md",
    python_requires=">=3.8",
    author="huang",
    license="MIThb",
    packages=find_packages(),
    install_requires=['pycryptodome', 'requests', 'asyncio'],
    include_package_data=True,
    keywords=['pytss'],
)