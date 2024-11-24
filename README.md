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
## 📂 Clone the Repository
To clone this repository, open your terminal and run:
```bash
    git clone https://github.com/Muzamil-Yaseen/TextExtractorGUI.git
   ```
Then, navigate into the project directory:
```bash
  cd TextExtractorGUI
   ```

## 📦 Install Dependencies
Navigate to the project directory and install the required dependencies by running:
```bash
  pip install -r requirements.txt
   ```

## ▶️ Running the Tool
After cloning the repository and installing the dependencies, you can start the GUI by running:
```bash
python text_extractor_gui.py
   ```
This will open a graphical user interface (GUI) where you can:

1) Select a file (PDF, image, or text).
2) Extract text.
3) Save the extracted text to a file.

## 📝 Usage Summary
1) Clone the repository
2) Install the dependencies
3) Run python text_extractor_gui.py to launch the GUI

## 🛠 Troubleshooting
If you encounter issues with pytesseract, ensure Tesseract OCR is installed and its executable is added to your system's PATH. On Windows, you can explicitly configure the path in the script:
```bash
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for more information.

## 🌟 About
Made by *Muzamil Yaseen*.
GitHub: https://github.com/Muzamil-Yaseen
