import re
import sys
from os import path
from codecs import open
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))


# check the supported interpreter version
if sys.version_info[0] != 3:
    sys.exit('Error, only Python 3.x supported')

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as descp_file:
    long_description = descp_file.read()


# read file with given name
def read(*names):
    with open(path.join(here, *names), encoding='utf-8') as fp:
        return fp.read()


def find_version(*file_paths):
    """Method to find current source code version."""
    version_file = read(*file_paths)
    version_match = re.search(r"^version = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


README = open(path.join(here, 'README.md')).read()

setup(
    name='Password factory',
    author="Rameez Hussain",
    author_email="hussain.gik294@gmail.com",
    version=find_version("app/", "metadata.py"),
    description='App to generate passwords on demand',
    long_description=long_description,

    # project home page
    url='https://github.com/ramigiki/passwordfactory',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages('app'),
    package_dir={'': 'app'},
    install_requires=[
        "Flask==2.2.1",
        "apispec==5.2.2",
        "requests==2.28.1",
        "flake8==5.0.4",
        "flask-apispec==0.11.1",
        "pyflakes==2.5.0",
        "pylint==2.14.5",
        "Flask-Cors==3.0.10",
        "uWSGI==2.0.20",
        "python-dotenv==0.20.0",
        "Flask-RESTful==0.3.9",
        "marshmallow==3.9.0",
        "black==22.6.0"
    ],
    include_package_data=True,
    zip_safe=False,
)
