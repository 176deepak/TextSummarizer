from setuptools import setup, find_packages
from typing import List

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "Summarizer"
AUTHOR_USER_NAME = "176deepak"
SRC_REPO = "src"

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="Summarizer",
    version="0.0.1",
    author="Deepak Saini",
    author_email="deepak170602@gmail.com",
    description="A small python package for Text Summaization.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    }, 
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
