from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.2'
DESCRIPTION = 'Copy karne ke liye'

# Setting up
setup(
    name="closeCV",
    version=VERSION,
    author="NeuralNine (Florian Dedov)",
    author_email="jack2018@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",

    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

