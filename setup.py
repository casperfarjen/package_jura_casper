setuptools.setup(
    name="rv_curve_Casper",
    version="0.1",
    author="Casper Farret Jentink",
    author_email='casper.farret@gmail.com',
    description="Plot all RV curves that you want",
    packages=setuptools.find_packages(),
    install_requires=["numpy","matplotlib"],
    classifiers=["Programming Language :: Python :: 3"],
)