import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "shadowmode",
    author = "shadow_mode team",
    description = "tools for shadowmode",
    packages = setuptools.find_packages(),
    python_requires = ">=3.6"
)