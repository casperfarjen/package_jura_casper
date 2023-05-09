import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rv_curve_Casper",
    version="0.1",
    author="Casper Farret Jentink",
    author_email='casper.farret@gmail.com',
    description="Plot all RV curves that you want",
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/casperfarjen/package_jura_casper",
    install_requires=["numpy","matplotlib"],
    classifiers=["Programming Language :: Python :: 3",
                "Operating System :: OS Independent"],
)
