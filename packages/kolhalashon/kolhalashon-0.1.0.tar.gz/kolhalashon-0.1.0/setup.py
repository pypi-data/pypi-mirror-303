from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as he:
    long_description = he.read()

setup(
    name="kolhalashon",
    version="0.1.0",
    author="ZVI SHTEINMAN",
    author_email="T7647986@GMAIL.COM",
    description="Python wrapper for Kol Halashon API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZviCode/KolHalashonApi",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests==2.32.3",
        "python-dotenv==1.0.1"
    ],
)