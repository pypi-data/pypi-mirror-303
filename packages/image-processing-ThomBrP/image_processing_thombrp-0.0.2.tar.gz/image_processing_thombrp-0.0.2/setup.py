from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_ThomBrP",
    version="0.0.2",
    author="ThomBrP",
    author_email="Thomasbrp@gmail.com",
    description="DIO Study about python packages",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThomBrP/Engenharia-de-Dados-com-Python-DIO",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8"
)