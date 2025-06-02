"""
PDF Merger GUI Application

This project is a simple graphical user interface (GUI) tool to select multiple PDF files
and combine them into a single PDF file. It uses the PyPDF2 library for PDF processing
and Tkinter for the GUI. 

Users can select PDFs from their file system, see the selected files listed,
and save the merged output as a new PDF file.

This can be integrated as a module in a larger application or used standalone.
"""

import PyPDF2
from tkinter import Tk, Label, Button, filedialog, messagebox

# Global variable to store the list of selected PDF file paths
archivos_pdf = []

def seleccionar_archivos():
    """
    Opens a file dialog to select multiple PDF files.
    Updates the label with the selected file names or shows a message if none selected.
    """
    global archivos_pdf
    archivos_pdf = filedialog.askopenfilenames(
        title="Select PDF files to merge",
        filetypes=[("PDF files", "*.pdf")]
    )
    if archivos_pdf:
        archivos_seleccionados.config(
            text="Selected files: " + ", ".join(archivos_pdf)
        )
    else:
        archivos_seleccionados.config(text="No files selected.")

def guardar_archivo():
    """
    Opens a save dialog to choose the output filename for the merged PDF.
    Combines the selected PDF files into one and saves it.
    Shows appropriate message dialogs for success, errors, or warnings.
    """
    if not archivos_pdf:
        messagebox.showerror("Error", "No PDF files have been selected.")
        return
    
    archivo_guardado = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF file", "*.pdf")],
        title="Save merged PDF file"
    )
    if archivo_guardado:
        try:
            pdf_merger = PyPDF2.PdfMerger()
            for pdf in archivos_pdf:
                pdf_merger.append(pdf)

            pdf_merger.write(archivo_guardado)
            pdf_merger.close()

            messagebox.showinfo("Success", f"PDF files successfully merged into:\n{archivo_guardado}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while merging files:\n{e}")
    else:
        messagebox.showwarning("Warning", "No output file was selected to save.")

# --- GUI Setup ---

# Create main application window
ventana = Tk()
ventana.title("PDF Merger")

# Set a light background color for the window
ventana.config(bg="#f0f0f0")

# Instruction label with styling
label_instrucciones = Label(
    ventana,
    text="Select the PDF files you want to merge.",
    bg="#f0f0f0",
    fg="#333333",
    font=("Arial", 12, "bold")
)
label_instrucciones.pack(pady=10)

# Button to open file dialog for selecting PDFs
boton_seleccionar = Button(
    ventana,
    text="Select Files",
    command=seleccionar_archivos,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12),
    relief="flat",
    padx=10,
    pady=5
)
boton_seleccionar.pack(pady=10)

# Label to display selected files or info
archivos_seleccionados = Label(
    ventana,
    text="No files selected.",
    bg="#f0f0f0",
    fg="#333333",
    font=("Arial", 10)
)
archivos_seleccionados.pack(pady=10)

# Button to save the combined PDF file
boton_guardar = Button(
    ventana,
    text="Save Merged PDF",
    command=guardar_archivo,
    bg="#2196F3",
    fg="white",
    font=("Arial", 12),
    relief="flat",
    padx=10,
    pady=5
)
boton_guardar.pack(pady=20)

# Start the Tkinter event loop
ventana.mainloop()
