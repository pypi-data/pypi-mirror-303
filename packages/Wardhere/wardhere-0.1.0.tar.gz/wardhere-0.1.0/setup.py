from setuptools import setup, find_packages

setup(
    name="Wardhere",            # Package name
    version="0.1.0",                # Initial version
    author="Badrudin Mohamed Ali",
    author_email="badrudin.dev@gmail.com",
    description="A simple Python package to greet people. Note: I created this package for testing package creation in Python.",
    packages=find_packages(),       # Automatically discover packages
    install_requires=[],            # External dependencies (if any)
    url="https://packaging.python.org/en/latest/tutorials/packaging-projects/",
    classifiers=[                   # Metadata about the project
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
