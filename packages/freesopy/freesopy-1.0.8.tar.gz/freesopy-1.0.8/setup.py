from setuptools import setup
import pathlib

# Get the long description from the README file
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="freesopy",
    version="1.0.8",
    description="This is a Python package for the implementation of various equations of Free Space Optical Communication",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Shoaib,Deepak and Tanvi",
    packages=["freesopy"],
    install_requires=["numpy","matplotlib"],
)