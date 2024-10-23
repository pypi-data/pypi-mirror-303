# setup.py to deploy gw_foresight to PyPi
from setuptools import setup, find_packages

setup(
    name="gw-foresight",
    version="0.3.0",
    packages=find_packages(),  # This automatically finds packages in the subdirectory.
    author="Glasswall",
    author_email="support@glasswall.com",
    description="Glasswall Foresight API Python Wrapper",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
