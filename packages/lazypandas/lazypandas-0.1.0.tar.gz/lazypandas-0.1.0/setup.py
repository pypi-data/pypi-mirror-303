
from setuptools import setup, find_packages

setup(
    name="lazypandas",
    version="0.1.0",
    description="High-performance, lazy evaluation library for dataframes, optimized for large datasets and complex transformations.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Siddharth Krishnan",
    author_email="sid@sidkrishnan.com",
    url="https://github.com/sidkris/lazypandas",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0",
        "numpy>=1.18",
        "psutil>=5.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires='>=3.6',
)
