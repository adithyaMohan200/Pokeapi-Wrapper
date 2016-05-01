from setuptools import setup, find_packages
from codecs import open
from os import path
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = "PokeapiWrapper",
    version = "0.9",
    packages = ["pokeapi",],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ['requests'],

    # metadata for upload to PyPI
    author = "Adithya Mohan",
    author_email = "Socketphys@gmail.com",
    description = "This is a Pokeapi wrapper",
    license = "MIT",
    keywords = "pokeapi wrapper",
    url = "https://github.com/SocketPhys/Pokeapi-Wrapper",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)
