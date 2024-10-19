from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="igscrap",
    version="0.1.0",
    author="EBF Tech",
    author_email="ebftech22@gmail.com",
    description="A tool to download Instagram posts and send them to Zapier to save in Google Drive",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eliefrancois/igscrap",
    packages=find_packages(),
    install_requires=[
        "instaloader>=4.9.5",
        "requests>=2.28.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "igscrap=igscrap.main:main",
        ],
    },
)
