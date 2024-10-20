from setuptools import setup

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding='UTF-8') as fh:
    requirements = fh.read().split("\n")

setup(
    name="ini-google-search",
    version="1.0.0",
    author="Pyjri",
    author_email="admin@pyjri.com",
    description="A Python library for scraping the Google search engine.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.pyjri.com/",
    packages=["ini-google-search"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[requirements],
    include_package_data=True,
)
