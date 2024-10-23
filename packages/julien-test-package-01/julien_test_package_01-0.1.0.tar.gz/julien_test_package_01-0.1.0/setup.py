from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of the README file for long_description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='julien-test-package-01',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],  # Add dependencies here
    description='A description of your package',
    long_description=long_description,  # Include long description here
    long_description_content_type='text/markdown',  # Set to 'text/markdown' for Markdown files
    author='Your Name',
    author_email='youremail@example.com',
    url='https://github.com/yourusername/your-repo',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
