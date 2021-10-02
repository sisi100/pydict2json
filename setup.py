import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements/dev.txt", mode="r", encoding="utf-8") as requirements:
    dev_packages = requirements.read().splitlines()

with open("requirements/prod.txt", mode="r", encoding="utf-8") as requirements:
    packages = requirements.read().splitlines()

setuptools.setup(
    name="pydict2json",
    version="0.0.1",
    description="Convert Python dict to JSON",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="sisii",
    package_dir={"": "pydict2json"},
    packages=["pydict2json"],
    install_requires=packages,
    extras_require={"dev": dev_packages[1:], "test": ["pytest"]},
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8" "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={"console_scripts": ["pydict2json = pydict2json:main"]},
)
