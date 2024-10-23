from setuptools import setup, find_packages
from pathlib import Path

# Read the README.md file with the correct encoding
long_description = Path("README.md").read_text(encoding='utf-8')

setup(
    name="AuthVault",
    version='3',  # Package version
    packages=find_packages(),  # Automatically find the package directory
    install_requires=[
        'requests',         # HTTP library for API requests
        'gspread',          # Google Sheets API interaction
        'oauth2client',     # OAuth 2.0 client for authentication
        'cryptography',     # For encryption, if used
        'psutil',           # For system and process utilities
        'pyarmor',          # Used for obfuscation (as mentioned)
        # Add other libraries you need here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",  # Specify that the long description is in Markdown
    author="QSXD",
    author_email="n3v1n22@gmail.com",
    url="",  # Add your URL if the project is hosted somewhere
)
