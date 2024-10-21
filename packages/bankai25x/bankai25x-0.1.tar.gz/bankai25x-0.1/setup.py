from setuptools import setup, find_packages

setup(
    name="bankai25x",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,  # Ensures non-code files (like PDFs) are included
    package_data={
        'bankai25x': ['ALL_PRACT_PROPER/*.pdf'],
	  'bankai25x': ['GUIDE/*.pdf'],
	  'bankai25x': ['ALL_PRACT_EASY/*.py'],
	  'bankai25x': ['IMPORTANT/*.pdf']

  # Specify that we want to include the PDF
    },
    description="A module with a PDF and Python file",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://example.com/mymodule",
)
