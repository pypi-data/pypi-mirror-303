from setuptools import *
import os
import codecs
here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='DENOLIB_D18',
    version='0.1.4',
    author='DENO',
    author_email='vinhytb3010@gmail.com',
    description='Thư Viện Về Python Cơ Bản',
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    classifiers =  [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)