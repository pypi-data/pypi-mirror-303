# setup.py
from setuptools import setup, find_packages

setup(
    name="gloveisglo",
    version="0.1.1-rc.1",
    packages=find_packages(),
    install_requires=[],
    author="Biplav",
    author_email="your-email@example.com",
    description="A sample Python project",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/my_sample_project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
