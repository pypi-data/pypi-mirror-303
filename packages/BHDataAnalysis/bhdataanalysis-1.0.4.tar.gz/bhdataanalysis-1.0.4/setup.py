from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.4'
DESCRIPTION = 'Header files for Data Analysis preprocessing methods'
LONG_DESCRIPTION = 'A header file which contains preprocessing and other methods for data analysis'

# Setting up
setup(
    name="BHDataAnalysis",
    version=VERSION,
    author="Developer - Skanda Chandrashekar",
    author_email="skanda.chandrashekar@bakerhughes.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    install_requires=['spacy','nltk','pandas'],
    keywords=['data analysis', 'preprocessing', 'methods', 'headerfiles', 'python'],
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)