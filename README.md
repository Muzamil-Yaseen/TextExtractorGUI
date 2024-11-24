# TextExtractorGUI

This repository offers a **Python-based GUI tool** for extracting text from PDF files, images, or text files using `pytesseract`, `pdfplumber`, and `Pillow`. The GUI allows users to select files, extract text, and save the output in a text file. It provides a user-friendly interface for handling text extraction tasks efficiently.

---

## 📥 Installation

### Prerequisites

1. Ensure you have **Python 3.7 or higher** installed. Download Python from the [official Python website](https://www.python.org/downloads/).
2. Install **Tesseract OCR** for image processing:
   - **Windows**: Download and install Tesseract from [Tesseract OCR GitHub Releases](https://github.com/tesseract-ocr/tesseract/releases).
   - **MacOS**: Use Homebrew to install Tesseract:
     ```bash
     brew install tesseract
     ```
   - **Linux**: Install Tesseract using your package manager:
     ```bash
     sudo apt install tesseract-ocr
     ```

3. Verify your Python and pip installations by running:
   ```bash
   python --version
   pip --version
