from setuptools import setup, find_packages

setup(
    name='excel_reformatter',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'openpyxl',  # Required for reading/writing Excel files
    ],
    description='A library for reformatting Excel files where all worksheets will be merged into one.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/BastianKuelzer/excel_reformatter',  # Replace with your GitHub repo
    author='Bastian Külzer',
)