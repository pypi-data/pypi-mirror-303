"""setup midea-lan."""

from pathlib import Path

import setuptools

readme = Path("README.md")
with readme.open(encoding="utf-8") as fh:
    long_description = fh.read()

requirements = Path("requirements.txt")
with requirements.open(encoding="utf-8") as fp:
    requires = fp.read().splitlines()

version: dict = {}
version_file = Path("midea_lan", "version.py")
with version_file.open(encoding="utf-8") as fp:
    exec(fp.read(), version)  # noqa: S102


setuptools.setup(
    name="midea-lan",
    version=version["__version__"],
    author="wuwentao, rokam, chemelli74, Necroneco",
    author_email="wuwentao2000@126.com, lucas@mindello.com.br",
    description="Control your Midea M-Smart appliances via local area network",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/midea-lan/midea-lan",
    install_requires=requires,
    packages=setuptools.find_packages(
        include=["midea_lan", "midea_lan.*"],
        exclude=["tests", "tests.*"],
    ),
    entry_points={
        "console_scripts": [
            "midea_lan = midea_lan.cli:main",
        ],
    },
    python_requires=">=3.11",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
