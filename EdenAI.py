import json
import requests
from PIL import Image
import io
import base64

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjFkNTkzYzAtNzg5YS00Y2JlLTlkMWQtY2FiOTkwMzQxY2UwIiwidHlwZSI6ImFwaV90b2tlbiJ9.Wuuo9toxCAsEEJql85dPjEVqRn1Mwbz3PBv-zVrXmys"}

def generate_Image(prompt,i):

    url = "https://api.edenai.run/v2/image/generation"              	 
    payload = {
    "providers": "openai",
    "text": prompt,
    "resolution" : "512x512"
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)

    img_data = result['openai']['items'][0]['image']

    # Decode the Base64 string into bytes
    image_bytes = base64.b64decode(img_data)

    # Create a BytesIO object to work with Pillow
    image_io = io.BytesIO(image_bytes)

    # Open and display the image using Pillow
    image = Image.open(image_io)
    #image.show()

    # If you want to save the image to a file
    image.save("Images/decoded_image"+str(i)+".jpg")
    return "Images/decoded_image"+str(i)+".jpg"


def get_keywords(text):
    url ="https://api.edenai.run/v2/text/keyword_extraction"
    payload = {
        "show_original_response": False,
        "fallback_providers": "",
        "providers": "amazon,microsoft", 
        "language": "en", 
        "text": text}

    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)
    return result['amazon']['items']
    print(result['amazon']['items'])



