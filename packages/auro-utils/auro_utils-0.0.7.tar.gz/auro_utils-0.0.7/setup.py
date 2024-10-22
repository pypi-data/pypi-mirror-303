#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = [
    "colorlog ",
    "rospkg",
    "loguru",
    "toml",
    "h5py",
    "numpy",
    "yappi",
    "gprof2dot",
    "pytest",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Herman Ye",
    author_email="hermanye233@icloud.com",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    description="Auro Utils is a utility package offering various practical supports for the Auromix application, such as enhanced logging capabilities and more.",
    install_requires=requirements,
    license="Apache Software License 2.0",
    include_package_data=True,
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="auro_utils",
    name="auro_utils",
    packages=find_packages(include=["auro_utils", "auro_utils.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/Hermanye996/auro_utils",
    version="0.0.7",
    zip_safe=False,
)
