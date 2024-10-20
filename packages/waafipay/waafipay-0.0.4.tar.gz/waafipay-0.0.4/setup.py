from setuptools import setup, find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="waafipay",                # Package name
    version="0.0.4",                # Package version
    author="Badrudin Mohamed Ali",
    author_email="badrudin.dev@gmail.com",
    description="A Python client for the WaafiPay API",  # Short description
    long_description=README,        # Use README.md as long description
    long_description_content_type="text/markdown",  # Content type of the long description
    packages=find_packages(),
    install_requires=[
        "requests",  # External dependencies
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
