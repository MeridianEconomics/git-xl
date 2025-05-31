"""Install git-xl as a python package"""
from setuptools import setup, find_packages

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = ""

# Load __version__ info:
exec(open("src/version.py", encoding="utf-8").read())

setup(
    name="gitxl",
    version=__version__,
    author="Felix Zumstein",
    author_email="felix.zumstein@zoomeranalytics.com",
    description="A Git Extension for Excel",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xlwings/git-xl",
    install_requires=open("requirements.txt").read().splitlines(),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    entry_points={
        "console_scripts": [
            "git-xl=gitxl.cli:main",
        ],
    },
)
