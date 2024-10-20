import pathlib
import setuptools

setuptools.setup(
    name='spindle',
    version='0.0.0',
    description="Package for computing the properties of classical magnetic systems",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Gustavo Sáez Cruz",
    author_email="virtualgluon@gmail.com",
    license="MIT",
    python_requires=">=3.12",
    install_requires=["numpy", "scipy", "matplotlib", "pathos"],
    packages=setuptools.find_packages(),
    include_package_data=True
)