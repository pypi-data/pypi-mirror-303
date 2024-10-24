import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="helloffyz",
    version="1.3.0",
    author="ffyz",
    url='https://github.com/xjgg1221/helloffyz-pypi',
    author_email="xj99gg@gmail.com",
    description="try to upload a pypi package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
