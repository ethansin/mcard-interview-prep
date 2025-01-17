from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip() and not line.startswith("#")]


setup(
    name="mcard_prep",  # Replace with your project name
    version="0.1.0",
    author="Ethan Sin",
    author_email="elsin@ucsc.edu",
    description="Practice for mcard job description.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ethansin/mcard-interview-prep",  # Replace with your repo URL
    packages=find_packages(),  # Automatically find packages
    install_requires=parse_requirements("requirements.txt"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
