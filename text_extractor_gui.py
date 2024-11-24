# File: text_extractor_gui.py
# Made by Muzamil
# GitHub: https://github.com/Muzamil-Yaseen

import os
import pytesseract
from tkinter import Tk, Label, Button, filedialog, messagebox, Text
from PIL import Image
from pdfplumber import open as open_pdf


def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from a PDF file."""
    try:
        with open_pdf(file_path) as pdf:
            text = ''.join(page.extract_text() for page in pdf.pages)
        return text.strip()
    except Exception as e:
        return f"Error reading PDF: {e}"


def extract_text_from_image(file_path: str) -> str:
    """Extract text from an image using OCR."""
    try:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return f"Error reading image: {e}"


def extract_text_from_txt(file_path: str) -> str:
    """Read text from a .txt file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text.strip()
    except Exception as e:
        return f"Error reading TXT file: {e}"


def save_text_to_file(text: str, output_path: str):
    """Save extracted text to a file."""
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(text)
        messagebox.showinfo("Success", f"Text successfully saved to {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving text: {e}")


class TextExtractorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Extractor")

        # File selection
        self.label = Label(root, text="Select a file to extract text", font=("Arial", 14))
        self.label.pack(pady=10)

        self.select_button = Button(root, text="Select File", command=self.select_file, font=("Arial", 12))
        self.select_button.pack(pady=5)

        self.extract_button = Button(root, text="Extract Text", command=self.extract_text, font=("Arial", 12), state="disabled")
        self.extract_button.pack(pady=5)

        self.save_button = Button(root, text="Save Extracted Text", command=self.save_text, font=("Arial", 12), state="disabled")
        self.save_button.pack(pady=5)

        # Text display
        self.text_area = Text(root, wrap="word", font=("Arial", 12), height=15, width=60)
        self.text_area.pack(pady=10)
        self.text_area.config(state="disabled")

        # File paths
        self.file_path = None
        self.extracted_text = None

    def select_file(self):
        """Open file dialog to select a file."""
        file_types = [("PDF files", "*.pdf"), ("Image files", "*.jpg;*.jpeg;*.png"), ("Text files", "*.txt")]
        self.file_path = filedialog.askopenfilename(filetypes=file_types)

        if self.file_path:
            self.extract_button.config(state="normal")
            self.label.config(text=f"Selected: {os.path.basename(self.file_path)}")

    def extract_text(self):
        """Extract text from the selected file."""
        if not self.file_path:
            messagebox.showerror("Error", "No file selected.")
            return

        file_extension = os.path.splitext(self.file_path)[1].lower()
        if file_extension == '.pdf':
            self.extracted_text = extract_text_from_pdf(self.file_path)
        elif file_extension in ['.jpg', '.jpeg', '.png']:
            self.extracted_text = extract_text_from_image(self.file_path)
        elif file_extension == '.txt':
            self.extracted_text = extract_text_from_txt(self.file_path)
        else:
            messagebox.showerror("Error", "Unsupported file type.")
            return

        self.text_area.config(state="normal")
        self.text_area.delete("1.0", "end")
        self.text_area.insert("1.0", self.extracted_text)
        self.text_area.config(state="disabled")
        self.save_button.config(state="normal")
        messagebox.showinfo("Success", "Text extraction completed.")

    def save_text(self):
        """Save the extracted text to a file."""
        if not self.extracted_text:
            messagebox.showerror("Error", "No text to save.")
            return

        output_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                   filetypes=[("Text files", "*.txt")])
        if output_path:
            save_text_to_file(self.extracted_text, output_path)


if __name__ == "__main__":
    # Configure pytesseract if needed
    # pytesseract.pytesseract.tesseract_cmd = r"path_to_tesseract_executable"

    root = Tk()
    app = TextExtractorGUI(root)
    root.mainloop()
