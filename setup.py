# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my_lamb_data_pt5", # the name that you will install via pip
    version="1.0",
    author="Regina Dircio",
    author_email="reginadircio@gmail.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/RMDircio/LambdaData-RMDircio",
    #keywords="",
    packages= ["my_lambdata"] # find_packages()
)