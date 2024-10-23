from setuptools import setup, find_packages

setup(
    name="fermata-edgedet-cli",
    version="0.1",
    packages=find_packages(),  # Automatically find packages like 'fermata'
    install_requires=[
        "Flask",
        "requests"
    ],
    entry_points={
        'console_scripts': [
            'fermata=fermata.cli:main',  # This defines the 'fermata' command and links it to fermata.cli:cli
        ],
    },
    author="Daniel George",
    description="CLI tool for authenticating and calling the Fermata API",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dageorge1111/fermata-cli",  # Optional
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
