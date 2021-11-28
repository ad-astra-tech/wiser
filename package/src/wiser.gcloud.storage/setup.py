import setuptools
from pathlib import Path

CURRENT_DIR = Path(__file__).parent

# Package metadata
name = ("wiser-gcloud-storage",)
version = ("0.0.1",)
author = ("Nicola Massarenti",)
author_email = ("nicola.massarenti@gmail.com",)
description = ("A `wiser` python package that wraps Google Cloud Storage services.",)

# Requirements and dependencies
requirements = [
    "numpy>=1.20.0",
    "google-cloud-storage>=1.42.0",
]
extra_requirements = dict()

dependencies = [
    "wiser-core",
]

# Setup
setuptools.setup(
    name=name,
    version=version,
    author=author,
    author_email=author_email,
    description=description,
    long_description=None,
    long_description_content_type="text/markdown",
    url="https://github.com/nicolamassarenti/wiser",
    project_urls={
        "Bug Tracker": "https://github.com/nicolamassarenti/wiser/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    extras_require=extra_requirements,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)
