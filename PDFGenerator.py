from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
from PIL import Image as PILImage
from io import BytesIO
import random
import os
from EdenAI import generate_Image, get_keywords
import time

def resetfolder():
    
    folder_path = "Images"  # Replace with the path to the folder you want to clear

    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted file: {filename}")
    except FileNotFoundError:
        print(f"The folder '{folder_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def start_pdf(paragraphs):
    resetfolder()
    print("Starting PDF...")
    keywords = []
    images = []
    for paragraph in paragraphs:
        keywords.append(get_keywords(paragraph))
    
    print("Keywords: listo")
    j = 0
    for listK in keywords:
        random.seed(int(time.time()))
        i = random.randint(0, len(paragraphs)-1)
        keyword = listK[i]['keyword']
        print(keyword)
        prompt = f"Image of {keyword}."
        images.append(generate_Image(prompt,j))
        j+=1
    
    print("Images: listo")
    GeneratePDF(paragraphs,images)

def GeneratePDF(paragraphs,images):

    # Create a PDF document
    pdf_filename = "Video2PDF.pdf"
    document = SimpleDocTemplate(pdf_filename, pagesize=letter)

    # Create a list to hold the content of the PDF
    content = []
    max_image_width = 300

    # Sample text content
    for i in range(len(paragraphs)):
        # Add text to the content list
        styles = getSampleStyleSheet()
        content.append(Paragraph(paragraphs[i], styles['Normal']))

        # Add an image to the content list
        image_filename = images[i]
        image = PILImage.open(image_filename)
        width, height = image.size
        # Resize the image if it's too large for the page
        if width > max_image_width:
            aspect_ratio = width / height
            new_width = max_image_width
            new_height = int(new_width / aspect_ratio)
            image = image.resize((new_width, new_height), PILImage.ANTIALIAS)

        img_buffer = BytesIO()
        image.save(img_buffer, format="JPEG")

        content.append(Image(img_buffer, width=new_width, height=new_height))

    # Build the PDF document
    document.build(content)

    print(f"PDF created: {pdf_filename}")


