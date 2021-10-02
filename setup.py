import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydict2json",
    version="0.0.1",
    description="Convert Python dict to JSON",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="sisii",
    package_dir={"": "pydict2json"},
    packages=setuptools.find_packages(where="pydict2json"),
    install_requires=["pyperclip", "fire"],
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
