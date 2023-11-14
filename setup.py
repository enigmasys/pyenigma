# Create a setup.py for the package
# Path: setup.py
from setuptools import setup, find_packages

setup(
    name="pyudcp",
    version="0.0.8",
    description="Python binding for Enigma CLI/ UDCP CLI",
    author="yogeshvu",
    author_email="yogesh.d.barve@vanderbilt.edu",
    packages=find_packages(),
    install_requires= ["datamodel-code-generator", "pydantic~=2.4.2"],
    python_requires=">=3.7",
    # entry_points={
    #     "console_scripts": [
    #         "pyudcp = src.pyudcp.enigmapy:main",
    #     ]
    # },
)

