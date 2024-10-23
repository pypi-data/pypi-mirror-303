from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="binwise",
    version="0.2.0",
    author="Viacheslav Barkov",
    author_email="viacheslav.barkov@uni-osnabrueck.de",
    description="Enable classification models for regression tasks and provide uncertainty estimation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/slavabarkov/binwise",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy",
        "scikit-learn",
    ],
)
