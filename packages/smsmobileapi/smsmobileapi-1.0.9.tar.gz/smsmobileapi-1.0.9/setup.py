# -*- coding: utf-8 -*-
# setup.py

from setuptools import setup, find_packages

setup(
    name="smsmobileapi",
    version="1.0.9",
    author="Quest-Concept",
    author_email="info@smsmobileapi.com",
    description="A module that allows sending SMS from your own mobile phone and receiving SMS on your mobile phone, all for free since the mobile plan is used",
    long_description=open("README.md", encoding="utf-8").read(),  # Spécification de l'encodage UTF-8
    long_description_content_type="text/markdown",
    url="https://github.com/smsmobileapi/smsmobileapi",  # Assurez-vous que l'URL est correcte
    packages=find_packages(),
    install_requires=[
        'requests',  # Dépendance à requests pour faire des requêtes HTTP
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
