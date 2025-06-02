# dev-portfolio
A project with tools to manage PDF documents using Python.


# PDF Management Tools

This project includes a set of Python tools to automate the management of PDF documents.

## Current Features

1. **File Renamer:**  
   Scans PDF files for the text pattern `ASSET ID: <number>` and renames the file using the extracted number.  
   Additionally, the renamer allows adding a **prefix** or **suffix** to the new filename.  
   Example: If the document contains `ASSET ID: 03356`, the file can be renamed to `PRE_03356_SUF.pdf` (where `PRE_` is the prefix and `_SUF` is the suffix).

2. **PDF Merger:**  
   Allows merging multiple PDF files into a single combined document.

## Planned Features

- A tool to read specific fields in PDF documents and compare them with a dataset.  
- Automatically move files to specific folders based on matching criteria.

## Technologies Used

- Python  
- PyPDF2 (or the library you use)  
- Other PDF processing libraries as needed  

## Purpose

This project is part of my personal portfolio to practice file manipulation and automation with Python.
