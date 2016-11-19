from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="sample",
    version="0.1.0",
    description="A simple web framework.",
    long_description=long_description,
    url="https://github.com/pypa/sampleproject",
    author="The Python Packaging Authority",
    author_email="pypa-dev@googlegroups.com",
    license="MIT",

    classifiers=[
        "Development Status :: 3 - Alpha",

        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",

        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3.5",
    ],

    keywords="sample setuptools development",

    packages=find_packages(exclude=["contrib", "docs", "tests"]),

    install_requires=["aiohttp", "aiohttp_autoreload", "aiorethink", "cerberus"],

    extras_require={
        "dev": ["check-manifest"],
        "test": ["coverage"],
    },

    scripts=["bin/brink"],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        "console_scripts": [
            "sample=sample:main",
        ],
    },
)
