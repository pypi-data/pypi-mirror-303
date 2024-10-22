from setuptools import setup, find_packages
import codecs
import os
VERSION = '0.0.2'
DESCRIPTION = 'DENO_STUDY_D18'

# Setting up
setup(
    name="DENO_STUDY_D18",
    version=VERSION,
    author="DENO",
    author_email="vinhytb3010@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    # long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['DENO','deno','study'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)