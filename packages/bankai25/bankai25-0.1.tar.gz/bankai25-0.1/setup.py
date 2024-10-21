from setuptools import setup, find_packages

setup(
    name="bankai25",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,  # Ensures non-code files (like PDFs) are included
    package_data={
        'bankai25': ['ALL_PRACT_PROPER/*.pdf'],
	  'bankai25': ['GUIDE/*.pdf'],
	  'bankai25': ['ALL_PRACT_EASY/*.py'],
	  'bankai25': ['IMPORTANT/*.pdf']

  # Specify that we want to include the PDF
    },
    description="A module with a PDF and Python file",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://example.com/mymodule",
)
