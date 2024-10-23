from setuptools import find_packages, setup

setup(
    name="truestate",
    version="0.5.62",
    description="A Python client for the Truestate API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="TrueState",
    author_email="support@truestate.io",
    url="https://docs.truestate.io/",
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=[
        "pydantic",
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Replace with your license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version requirement
)
