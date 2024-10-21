import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-lorem-ipsum",
    version="v2.0.0",
    author="Adam Birds",
    author_email="adam.birds@adbwebdesigns.co.uk",
    description="Generate Lorem Ipsum Text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adambirds/python-lorem-ipsum",
    project_urls={
        "Bug Tracker": "https://github.com/adambirds/python-lorem-ipsum/issues",
    },
    license="BSD-3-Clause",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(exclude=['tests']),
    include_package_data=True,
    python_requires=">=3.6",
)