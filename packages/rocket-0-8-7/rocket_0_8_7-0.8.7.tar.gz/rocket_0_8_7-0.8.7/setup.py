from setuptools import setup, find_packages

setup(
    name="rocket_0_8_7",
    version="0.8.7",
    author="aminaghandouz",
    author_email="a.ghandouz@esi-sba.dz",
    description="A package for simulating rockets and space shuttles.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/amaliahm/rocket", 
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
