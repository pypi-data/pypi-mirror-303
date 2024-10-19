from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="first_package_airton2junior",
    version="0.0.1",
    author="AIRTON JUNIOR",
    author_email="airton2junior@gmail.com",
    description="My first package",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Airton2Junior/FirstPackage.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)