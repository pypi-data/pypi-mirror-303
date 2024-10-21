# Import the function from reformatter.py so users can access it directly
from .reformatter import import_and_combine_excel_sheets

# Optionally include package metadata
__version__ = '0.1'
__author__ = 'Bastian Külzer'

# Define what gets exported when someone uses `from excel_reformatter import *`
__all__ = ['import_and_combine_excel_sheets']