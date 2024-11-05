import pytesseract
from PIL import Image
from app.image_processing import load_image, preprocess_image

def extract_text_from_image(file_path):
    """
    Extracts text from an image at the given file path.
    
    Args:
        file_path (str): Path to the image file.
    
    Returns:
        str: The extracted text from the image.
    """
    # Configure Tesseract path
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path if necessary

    # Load the image
    image = load_image(file_path)
    if image is None:
        return "Failed to load image."

    # Preprocess the image for better text extraction
    preprocessed_image = preprocess_image(image)
    custom_config = r'--oem 3 --psm 6'  
    # Use pytesseract to extract text from the image
    extracted_text = pytesseract.image_to_string(preprocessed_image, lang='eng+rus+kaz', config=custom_config)
    
    return extracted_text
