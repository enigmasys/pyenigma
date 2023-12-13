# Create a setup.py for the package
# Path: setup.py
from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


# Also include the readme.md file in the package


setup(
    name="pyudcp",
    version="0.3.0",
    description="Python binding for Enigma CLI/ UDCP CLI",
    author="yogeshvu",
    author_email="yogesh.d.barve@vanderbilt.edu",
    url="https://github.com/enigmasys/pyenigma",
    packages=find_packages(),
    include_package_data=True,
    install_requires= ["datamodel-code-generator", "pydantic~=2.4.2"],
    python_requires=">=3.7",
    long_description=long_description,
    long_description_content_type="text/markdown",


    # entry_points={
    #     "console_scripts": [
    #         "pyudcp = src.pyudcp.enigmapy:main",
    #     ]
    # },
)

