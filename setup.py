import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BringApi",
    version="0.1.0",
    author="Runningtoy",
    author_email="",
    description="Unofficial Bring! Api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/runningtoy/bring-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"]
    install_requires=["json"]
)
