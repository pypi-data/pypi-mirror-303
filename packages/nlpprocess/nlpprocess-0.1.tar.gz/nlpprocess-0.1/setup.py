# setup.py
from setuptools import setup, find_packages

setup(
    name='nlpprocess',               # Name of the package
    version='0.1',                   # Version of the package
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'spacy',
        'matplotlib',
        'spacy_cleaner',
        'tqdm',
        'think',
        'dill',
    ],
    
    author='Sina Heydari',
    author_email='sinaa.heydari.76@gmail.com',      
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='~=3.10',         
)
