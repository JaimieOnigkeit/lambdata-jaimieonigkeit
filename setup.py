from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my-lambdata-jaimieonigkeit",  # the name that you will install via pip
    version="1.1",
    author="Jaimie Onigkeit",
    author_email="jaimie.onigkeit@gmail.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # required if using a md file for long desc
    license="MIT",
    url="https://github.com/JaimieOnigkeit/lambdata-jaimieonigkeit",
    # keywords="",
    packages=find_packages()  # ["my_lambdata"]
)
