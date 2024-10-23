from setuptools import setup, find_packages

setup(
    name="mysql_module",  # Unique name for your package on PyPI
    version="0.1.0",  # Initial release version
    description="A Python module for interacting with MySQL databases",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  # To format README correctly on PyPI
    author="H-Rasheed",
    author_email="rsm878yourkhan@gmail.com",
    packages=find_packages(),  # Automatically finds and includes your mysql_module package
    install_requires=[  # Add dependencies here, if any
        "mysql-connector-python"
    ],
)
