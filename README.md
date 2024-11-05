# Text Extraction from Images Application

This project is a Python-based application with a graphical user interface (GUI) for extracting text from images. The app allows users to load an image, view the extracted text, and save the text as a DOCX or PDF file.

## Features
- **Image Loading**: Users can import images in formats such as PNG, JPG, or JPEG.
- **Text Extraction**: Extracts text from images using the Tesseract OCR engine.
- **Text Display**: The extracted text is displayed in a text box for easy viewing.
- **Save Options**: Users can save the extracted text as a DOCX or PDF file.

## Technologies Used
- **Python**: Core programming language.
- **Tkinter**: Used for building the GUI.
- **Pillow**: For image handling.
- **pytesseract**: For text extraction using Tesseract OCR.
- **python-docx**: For saving text as a DOCX file.
- **reportlab**: For generating PDF files.

## Folder Structure
```
text_extraction_app/
│
├── main.py                 # Entry point of the application
├── requirements.txt        # List of dependencies
├── README.md               # Project documentation
│
├── app/
│   ├── __init__.py         # Makes 'app' a Python package
│   ├── gui.py              # Contains the GUI implementation
│   ├── image_processing.py # Handles image loading and preprocessing
│   └── text_extraction.py  # Extracts text from images using pytesseract
│



── ../Tesseract-OCR/tessdata/       # (Optional) Folder to store Tesseract language data files
```

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd text_extraction_app
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Make sure Tesseract OCR is installed and configured on your system. You can download it from [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).

## Usage
1. Run the application:
   ```bash
   python main.py
   ```
2. Click "Import Image" to load an image and extract text.
3. View the extracted text in the text box.
4. Save the text as a DOCX or PDF file using the "Save Text as DOCX" or "Save Text as PDF" buttons.

## Notes
- Ensure Tesseract OCR is properly installed on your system.
- The background color and layout of the GUI can be customized to suit your preferences.