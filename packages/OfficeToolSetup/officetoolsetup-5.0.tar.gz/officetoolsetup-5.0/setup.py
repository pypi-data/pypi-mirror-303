from setuptools import setup, find_packages

# Read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="OfficeToolSetup",
    version="5.0",
    author="Rakicc",
    author_email="gpenmail@gmail.com",
    description="A collection of office tools for PDF and Excel manipulation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rakicc/Office_Tools_PyQt5",
    packages=find_packages(),
    install_requires=[
        # List your project's dependencies here
        "PyQt5",
        "openpyxl",
        "xlwings",
        "pywin32",
        # Add any other dependencies
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
    entry_points={
        'console_scripts': [
            'OfficeToolSetup=Office_Tools:main',  # Adjust this line to match your main function
        ],
    },
)
