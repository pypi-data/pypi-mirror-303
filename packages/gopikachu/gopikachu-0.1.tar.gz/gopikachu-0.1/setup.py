from setuptools import setup, find_packages

setup(
    name="gopikachu",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,  # Ensures non-code files (like PDFs) are included
    package_data={
        'gopikachu': ['ALL_PRACT_PROPER/*.pdf'],
	  'gopikachu': ['GUIDE/*.pdf'],
	  'gopikachu': ['ALL_PRACT_EASY/*.py'],
	  'gopikachu': ['IMPORTANT/*.pdf']

  # Specify that we want to include the PDF
    },
    description="A module with a PDF and Python file",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://example.com/mymodule",
)
