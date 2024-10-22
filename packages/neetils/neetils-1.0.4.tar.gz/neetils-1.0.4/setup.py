import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md"), "r", encoding="utf-8") as f:
    long_description = f.read()

setup(name="neetils",
      version="v1.0.4",
      author="tanknee",
      author_email="nee@tanknee.cn",
      description="A package for tools",
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=find_packages(include=["neetils", "neetils.*", "README.md"]),
      install_requires=[
          "tqdm",
          "loguru",
      ])
