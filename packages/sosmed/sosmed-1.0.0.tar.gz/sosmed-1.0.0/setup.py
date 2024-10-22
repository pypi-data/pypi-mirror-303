# MIT License

# Copyright (c) 2024 AyiinXd

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import re
import shutil
import sys
from setuptools import setup, find_packages

def clearFolder(folder):
    try:
        # Remove Directory
        if os.path.exists(folder):
            shutil.rmtree(folder)
    except Exception as e:
        print(e)

with open("sosmed/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

if sys.argv[-1] == "publish":
    clearFolder("build")
    clearFolder("dist")
    clearFolder("sosmed.egg-info")
    os.system("pip install twine setuptools")
    os.system("python3 setup.py sdist")
    os.system("twine upload dist/*")
    sys.exit()


setup(
    name="sosmed",
    version=version,
    description="Downloader Sosial Media - Multiple Platform and Asynchronous API in Python",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/AyiinXd/sosmed",
    download_url="https://github.com/AyiinXd/sosmed/releases/latest",
    author="AyiinXd",
    author_email="ayiin@gotgel.org",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=[
        "api",
        "scrapper",
        "downloader",
        "instagram",
        "tiktok",
        "twitter",
        "youtube"
    ],
    project_urls={
        "Tracker": "https://github.com/AyiinXd/sosmed/issues",
        "Community": "https://t.me/AyiinProjects",
        "Source": "https://github.com/AyiinXd/sosmed"
    },
    python_requires="~=3.7",
    package_data={
        "sosmed": ["py.typed"],
    },
    packages=find_packages(exclude=["tests*"]),
    zip_safe=False,
    install_requires=["aiofiles", "aiohttp"],
)
