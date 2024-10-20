from setuptools import setup, find_packages

setup(
    name="boyoke_encok",
    version="0.1.0",
    description="banner",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="Shairul alim",
    author_email="shairulalim644@gmail.com",
    packages=find_packages(),
    install_requires=[
        "colorama",
        "requests",
        "brotli",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
