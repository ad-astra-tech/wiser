import setuptools
from pathlib import Path

CURRENT_DIR = Path(__file__).parent

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = [
    "numpy>=1.20.0",
]
extra_requirements = dict(
    storage=[
        "google-cloud-storage>=1.42.0",
    ],
    firestore=[
        "google-cloud-firestore>=2.3.0",
    ],
)
all_extra_requirements = [
    item
    for key, value in extra_requirements.items()
    for item in extra_requirements[key]
]
extra_requirements["all"] = all_extra_requirements

setuptools.setup(
    name="wiser",
    version="0.1.2",
    author="Nicola Massarenti",
    author_email="nicola.massarenti@gmail.com",
    description="A python package designed to free the developers from the burden of common operations with cloud technologies.",
    long_description=long_description,
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
