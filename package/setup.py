import setuptools
from pathlib import Path

CURRENT_DIR = Path(__file__).parent

# Package metadata
name = "wiser"
version = "1.0.2"
author = "Nicola Massarenti"
author_email = "nicola.massarenti@gmail.com"
description = "Wraps cloud services wisely"

# Requirements, dependencies and namespaces
extra_requirements = {
    "gcloud-storage": ["wiser-gcloud-storage"],
    "gcloud-firestore": ["wiser-gcloud-firestore"],
}
dependencies = ["numpy"]
# Only include packages under the 'wiser' namespace. Do not include tests,
# benchmarks, etc.
packages = [
    package for package in setuptools.find_packages() if package.startswith("wiser")
]
namespaces = ["wiser"]

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
    install_requires=dependencies,
    extras_require=extra_requirements,
    namespace_packages=namespaces,
    packages=packages,
    python_requires=">=3.8",
    platforms="Posix; MacOS X; Windows",
    include_package_data=True,
    zip_safe=False,
)
