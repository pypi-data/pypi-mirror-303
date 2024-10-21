"doagain pkg"
import setuptools
from autoforge.__version__ import __version__

setuptools.setup(
    name="autoforge",
    version=__version__,
    author="SheldonGrant",
    author_email="sheldz.shakes.williams@gmail.com",
    packages=setuptools.find_packages(where="."),
    setup_requires=['setuptools>=75.1.0'],
    install_requires=[],
    python_requires=">=3.12"
)