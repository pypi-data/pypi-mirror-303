import os
import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from pdf2docx import Converter
from tkinter import messagebox

def pdf_to_word_with_formatting(pdf_path):
    """Convert PDF to Word document while preserving formatting and images."""
    # Create output file path (same directory, same name, with .docx extension)
    output_word_file = os.path.splitext(pdf_path)[0] + ".docx"
    
    # Create a converter object
    cv = Converter(pdf_path)
    
    # Convert PDF to Word document
    cv.convert(output_word_file, start=0, end=None)  # Converts all pages
    
    # Close the converter
    cv.close()

    return output_word_file

def on_file_drop(event):
    """Handle file drop event."""
    pdf_path = event.data.strip('{}')  # Strip the curly braces added by TkinterDnD
    
    if not pdf_path.lower().endswith('.pdf'):
        messagebox.showerror("Error", "Please drop a valid PDF file.")
        return
    
    try:
        # Convert the PDF to Word
        output_file = pdf_to_word_with_formatting(pdf_path)
        
        # Show success message
        messagebox.showinfo("Success", f"PDF has been converted to: {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main application window
root = TkinterDnD.Tk()  # Create a TkinterDnD window for drag-and-drop functionality
root.title("PDF to Word Converter")
root.geometry("400x200")

# Create a label to instruct the user
label = tk.Label(root, text="Drag and drop a PDF file here", font=("Helvetica", 14), pady=50)
label.pack(expand=True, fill=tk.BOTH)

# Bind the drag-and-drop event to the label
label.drop_target_register(DND_FILES)
label.dnd_bind('<<Drop>>', on_file_drop)

# Run the app
root.mainloop()
