from setuptools import setup, find_packages

setup(
    name="subsplease",
    version="1.0.3",
    packages=find_packages(),
    install_requires=[
        "httpx",
    ],
    description="A package for fetching and parsing episodes from SubsPlease API.",
    author="Praveen",
    author_email="pvnt20@gmail.com",
    url="https://github.com/praveensenpai/subsplease",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
