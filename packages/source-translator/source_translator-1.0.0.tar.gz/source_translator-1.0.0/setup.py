import pathlib
from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="source_translator",
    version="1.0.0",
    description="Module to translate Python source code into other programming languages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/mattbas/python-source-translator",
    author="Mattia \"Glax\" Basaglia",
    author_email="dev@dragon.best",  # Optional
    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Programming Language :: C++",
        "Programming Language :: JavaScript",
    ],
    keywords="transpiling, source convertion",
    package_dir={"": "src"},
    python_requires=">=3.9, <4",
    install_requires=[],
    entry_points={},
    project_urls={
        "Bug Reports": "https://gitlab.com/mattbas/python-source-translator/-/issues",
        "Source": "https://gitlab.com/mattbas/python-source-translator",
    },
)
