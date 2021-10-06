import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="massox",
    version="0.0.1",
    author="Nicola Massarenti",
    author_email="nicola.massarenti@gmail.com",
    description="Package distribution with several utilities for GCP connections, managing and other.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nicolamassarenti/massox",
    project_urls={
        "Bug Tracker": "https://github.com/nicolamassarenti/massox-package/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
