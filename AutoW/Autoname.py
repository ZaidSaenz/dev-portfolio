"""
This project is a desktop application that provides tools to manage PDF documents.
It allows users to select a folder containing PDFs and rename the files based on
text extracted from within the PDFs using a specified key. It also supports adding
prefixes and suffixes to the renamed files. The user interface is created using
PyWebView with a frontend served from an HTML file.

Modules used:
- tkinter: Used for displaying native folder selection dialogs.
- os: Used for file and directory path handling.
- pdfplumber: A library for extracting text from PDF files.
- re: Regular expressions for searching specific patterns in PDF text.
- webview: PyWebView to create a native GUI window that hosts HTML/JS frontend.
The project can be packaged into a standalone executable file using PyInstaller,
allowing it to be run directly from the terminal without requiring a Python environment.
"""
import tkinter as tk
from tkinter import filedialog
import os
import pdfplumber
import re
import webview

class Api:
    def __init__(self):
        # Store the currently selected folder path
        self.folder = ""

    def abrir_dialogo_carpeta(self):
        """
        Opens a native folder selection dialog using tkinter.
        Returns the selected folder path or None if cancelled.
        """
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        carpeta = filedialog.askdirectory()
        root.destroy()

        if carpeta:
            self.folder = carpeta
            return carpeta
        return None

    def seleccionar_carpeta(self, carpeta):
        """
        Sets the current folder path programmatically.
        Returns a confirmation string.
        """
        self.folder = carpeta
        return f"Folder set to: {carpeta}"

    def renombrar_pdfs(self, prefijo, sufijo, clave):
        """
        Renames PDF files in the selected folder.
        - prefijo: string to prepend to the new filename
        - sufijo: string to append to the new filename
        - clave: key to search for inside the PDF text to extract the identifier

        The method extracts text from each PDF, searches for the key followed by an
        alphanumeric identifier, then renames the file accordingly.
        Returns a dictionary with the count of renamed files or an error.
        """
        if not self.folder or not clave:
            return {"error": "Folder and key are required"}

        # List all PDF files in the folder
        archivos = [f for f in os.listdir(self.folder) if f.lower().endswith(".pdf")]
        renombrados = 0

        for archivo in archivos:
            ruta_pdf = os.path.join(self.folder, archivo)
            try:
                # Open the PDF and extract all text from its pages
                with pdfplumber.open(ruta_pdf) as pdf:
                    texto = "".join(p.extract_text() or "" for p in pdf.pages)

                # Build regex pattern to find the key followed by identifier
                patron = re.escape(clave) + r'\s*([A-Za-z0-9]+)'
                resultado = re.search(patron, texto)
                valor_extraido = resultado.group(1) if resultado else None

                if valor_extraido:
                    nuevo_nombre = f"{prefijo}{valor_extraido}{sufijo}.pdf"
                    nueva_ruta = os.path.join(self.folder, nuevo_nombre)

                    # Skip renaming if the new filename already exists
                    if os.path.exists(nueva_ruta):
                        continue

                    # Rename the file
                    os.rename(ruta_pdf, nueva_ruta)
                    renombrados += 1

            except Exception as e:
                print(f"Error processing {archivo}: {e}")

        return {"renamed": renombrados}


if __name__ == '__main__':
    api = Api()

    # Get absolute path of the current script's directory
    base_dir = os.path.abspath(os.path.dirname(__file__))

    # Path to the frontend HTML file inside the 'frontcss' folder
    html_file = os.path.join(base_dir, "frontcss", "index.html")

    # Raise an error if the HTML file is not found
    if not os.path.exists(html_file):
        raise FileNotFoundError(f"HTML file not found: {html_file}")

    # Create the GUI window with PyWebView pointing to the HTML frontend
    window = webview.create_window(
        "Rename PDFs with PyWebView",
        html_file,
        js_api=api,
        width=900,
        height=700
    )

    # Start the PyWebView event loop
    webview.start()

