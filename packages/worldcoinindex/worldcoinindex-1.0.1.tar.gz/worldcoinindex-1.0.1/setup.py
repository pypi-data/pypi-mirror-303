import pathlib
import setuptools

setuptools.setup(
    name="worldcoinindex",
    version="1.0.1",
    description="A lightweight wrapper for the WorldCoinIndex Cyptocoin API",
    long_description=pathlib.Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://www.worldcoinindex.com/apiservice",
    author="Pranav Chaturvedi",
    author_email="pranavhfs1@gmail.com",
    maintainer="PranavChaturvedi",
    license="MIT",
    project_urls={
        "Homepage": "https://www.worldcoinindex.com/apiservice",
        "Documentation": "https://github.com/PranavChaturvedi/worldcoinindex/blob/main/README.md",
        "Repository": "https://github.com/PranavChaturvedi/worldcoinindex",
    },
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    packages=setuptools.find_packages(),
    include_package_data=True,
)
