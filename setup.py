from setuptools import setup
from os import path

summary = "Tool for automated Instagram interactions"
project_homepage = "https://github.com/timgrossmann/InstaPy"
here = path.abspath(path.dirname(__file__))




setup(
    name="instapy",
    version=metadata["version"],
    description=summary,
    long_description=documentation,
    long_description_content_type="text/markdown",
    author=u"Tim Großmann",)
