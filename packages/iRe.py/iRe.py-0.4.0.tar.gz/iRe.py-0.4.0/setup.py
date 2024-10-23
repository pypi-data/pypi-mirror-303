from setuptools import setup, find_packages

setup(
    name="iRe.py",
    version="0.4.0",
    description="Export tables and plots from Jupyter notebooks, along with metadata for embedding interactive tables in downstream apps.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=open("requirements.txt", "r").read(),
    extras_require={
        "plotly": "plotly",
        "test": open("requirements-dev.txt", "r").read(),
    },
    license="MIT",
    author="Ryan Williams",
    author_email="ryan@runsascoded.com",
    url="https://gitlab.com/runsascoded/ire/py",
)
