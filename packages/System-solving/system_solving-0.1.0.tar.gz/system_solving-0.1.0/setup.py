from setuptools import setup, find_packages
setup(
    name="System-solving",  # Required: the name of your package
    version="0.1.0",  # Required: the version of your package
    author="Your Name",  # Required: your name or organization
    author_email="your.email@example.com",  # Required: your email address
    description="A simple package",  # Required: a short description of the package
    packages=find_packages(),  # Required: the packages to include in the distribution
    python_requires='>=3.6',  # Required: specify the minimum Python version supported
)