from PIL import Image

def load_image(file_path):
    """
    Loads an image from the given file path.
    
    Args:
        file_path (str): Path to the image file.
    
    Returns:
        Image: An Image object loaded from the file.
    """
    try:
        image = Image.open(file_path)
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def preprocess_image(image):
    """
    Preprocesses the image for text extraction.
    
    Args:
        image (Image): The PIL Image object to preprocess.
    
    Returns:
        Image: The preprocessed Image object.
    """
    # Convert the image to grayscale
    image = image.convert("L")
    
    # Additional preprocessing steps can be added here
    # For example: resizing, thresholding, etc.
    
    return image