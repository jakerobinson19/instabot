from setuptools import setup
from os import path

summary = "Tool for automated Instagram interactions"
project_homepage = "https://github.com/jakerobinson19/instabot"
here = path.abspath(path.dirname(__file__))

setup(
     name='instabot',  
     version='1.0',
     scripts=['instabot'] ,
     author="Jake Robinson",
     author_email="jakerobinson19@gmail.com",
     description="Automated bot for instagram using selenium",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url=project_homepage,
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )
