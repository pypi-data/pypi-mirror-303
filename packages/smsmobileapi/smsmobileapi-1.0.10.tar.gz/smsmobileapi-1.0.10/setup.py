# setup.py

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="smsmobileapi",
    version="1.0.10",
    author="Quest-Concept",
    author_email="info@smsmobileapi.com",
    description="A module that allows sending SMS from your own mobile phone and receiving SMS on your mobile phone, all for free since the mobile plan is used",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/smsmobileapi/smsmobileapi",
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
