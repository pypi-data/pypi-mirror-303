import codecs
import os
from setuptools import setup, find_packages

# these things are needed for the README.md show on pypi (if you dont need delete it)
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# you need to change all these
VERSION = '0.0.12'
DESCRIPTION = 'Consolidation package for daily use'

setup(
    name="gqxls",
    version=VERSION,
    author="S Liao",
    author_email="shunliaopetroleum@163.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    license="GNU General Public License v3.0",
    project_urls={
        'Source': 'https://github.com/891011well/gqxls',
        "Bug Tracker": "https://github.com/891011well/gqxls/issues",
    },
    packages=find_packages(),
    install_requires=['pillow<=10.4.0','pymupdf<=1.24.11','urllib3<=2.2.2','bs4<=4.12.3'],
    keywords=['python', 'gqxls'],
    classifiers=[  # see https://pypi.org/classifiers/
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Programming Language :: Python :: 3.11",
    ],
    platforms='any',
    python_requires='>=3.6',
)
