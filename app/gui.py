import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from app.text_extraction import extract_text_from_image
from docx import Document
from reportlab.pdfgen import canvas

class TextExtractionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Set up the main window
        self.title("Text Extraction from Images")
        self.configure(bg="#e6fff5")  # Changed background color to light pastel blue
        
        # Set the initial window size and center it on the screen
        window_width = 800
        window_height = 700  # Reduced height to adjust layout
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # Initialize save buttons as None (they will be created after image load)
        self.save_docx_button = None
        self.save_pdf_button = None
        
        # Create UI components
        self.create_widgets()
    
    def create_widgets(self):
        # Top part: Image display area
        self.image_label = tk.Label(self, bg="#e6f7ff")  # Match the new background color
        self.image_label.pack(pady=10)
        
        # Button to import an image
        self.import_button = tk.Button(
            self, text="Import Image", command=self.import_image,
            bg="#4CAF50", fg="white", font=("Arial", 12, "bold"),
            activebackground="#45a049", activeforeground="white"
        )
        self.import_button.pack(pady=10)
        
        # Horizontal line separator
        self.separator = tk.Frame(self, height=2, bd=1, relief="sunken", bg="#cccccc")
        self.separator.pack(fill="x", padx=5, pady=5)
        
        # Reduced size for the text box
        self.text_box = tk.Text(self, wrap="word", font=("Arial", 11), bg="#ffffff", fg="#333333", height=15)
        self.text_box.pack(expand=True, fill="both", padx=10, pady=10)
    
    def import_image(self):
        # Open file dialog to select an image
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            # Load the image and display it
            image = Image.open(file_path)
            image.thumbnail((400, 400))
            img_tk = ImageTk.PhotoImage(image)
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk
            
            # Extract text from the image
            extracted_text = extract_text_from_image(file_path)
            
            # Display the extracted text in the text box
            self.text_box.delete(1.0, tk.END)
            self.text_box.insert(tk.END, extracted_text)
            
            # Create and show "Save" buttons if they haven't been created yet
            if not self.save_docx_button:
                # Frame for Save Buttons
                self.button_frame = tk.Frame(self, bg="#e6f7ff")  # Match the new background color
                self.button_frame.pack(pady=5)
                
                self.save_docx_button = tk.Button(
                    self.button_frame, text="Save Text as DOCX", command=self.save_text_as_docx,
                    bg="#2196F3", fg="white", font=("Arial", 12, "bold"),
                    activebackground="#1976D2", activeforeground="white"
                )
                self.save_docx_button.pack(side="left", padx=10)
                
                self.save_pdf_button = tk.Button(
                    self.button_frame, text="Save Text as PDF", command=self.save_text_as_pdf,
                    bg="#FF5722", fg="white", font=("Arial", 12, "bold"),
                    activebackground="#E64A19", activeforeground="white"
                )
                self.save_pdf_button.pack(side="left", padx=10)
    
    def save_text_as_docx(self):
        # Open file dialog to save the text as a DOCX file
        file_path = filedialog.asksaveasfilename(defaultextension=".docx",
                                                 filetypes=[("DOCX files", "*.docx"), ("All files", "*.*")])
        if file_path:
            # Get the text from the text box
            text_content = self.text_box.get(1.0, tk.END)
            
            # Create a DOCX document and add the text
            doc = Document()
            doc.add_paragraph(text_content)
            doc.save(file_path)
    
    def save_text_as_pdf(self):
        # Open file dialog to save the text as a PDF file
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                 filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")])
        if file_path:
            # Get the text from the text box
            text_content = self.text_box.get(1.0, tk.END)
            
            # Create a PDF document and add the text
            c = canvas.Canvas(file_path)
            c.drawString(100, 750, "Extracted Text:")
            text_object = c.beginText(100, 730)
            text_object.setFont("Helvetica", 10)
            text_object.textLines(text_content)
            c.drawText(text_object)
            c.save()

# Create and run the application
if __name__ == "__main__":
    app = TextExtractionApp()
    app.mainloop()