from setuptools import setup, find_packages

setup(
    name="coverage-control-simulator",
    version="0.1.0",
    description="A Python package for coverage control using Voronoi partitions",
    author="Muhammad Hanif",
    author_email="mhaniffarhat@gmail.com",
    url="https://github.com/mhd-hanif/coverage-control-simulator",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "pandas"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
