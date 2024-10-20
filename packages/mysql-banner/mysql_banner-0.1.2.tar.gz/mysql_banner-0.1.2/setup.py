from setuptools import setup, find_packages

setup(
    name="mysql-banner",
    version="0.1.2",
    description="banner",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="Mysql Project",
    author_email="mysqlproject98@gmail.com",
    packages=find_packages(),
    install_requires=[
        "colorama",
        "requests",
        "brotli",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
