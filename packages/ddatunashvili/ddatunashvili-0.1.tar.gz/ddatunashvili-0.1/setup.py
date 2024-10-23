from setuptools import setup, find_packages

setup(
    name="ddatunashvili",  # Package name
    version="0.1",
    packages=find_packages(),
    description="A simple Base class package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/ddatunashvili",  # Your repository URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
