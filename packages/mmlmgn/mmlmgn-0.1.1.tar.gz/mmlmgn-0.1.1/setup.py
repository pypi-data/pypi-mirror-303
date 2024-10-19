from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.1.1"
DESCRIPTION = "Hypergraph contrastive learning framework for multiple similarity modalities"
LONG_DESCRIPTION = "A package that demos mmlmgn model with Mdata."

# Setting up
setup(
    name="mmlmgn",
    version=VERSION,
    author="axin",
    author_email="xinfei106@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    url="https://github.com/1axin/MML-MGNN",
    install_requires = [
        "numpy>=1.22.4,<2.0",
        "pandas>=2.2.3",
        "scikit-learn>=1.5.2",
        "scipy>=1.13.1",
        "torch>=1.10.0",
        "joblib>=1.4.2"
    ],
    keywords=["Multiple Similarity Modes", "HGCN", "Hypergraph Contrastive Learning"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    package_data={"": ["*.csv", "*.txt", ".toml"]},
    include_package_data=True,
)
