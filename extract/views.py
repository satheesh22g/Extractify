from django.shortcuts import render
from .models import ExtractedData
import pytesseract
from PIL import Image
from io import BytesIO
pytesseract.pytesseract.tesseract_cmd = r'G:\tessaract\tesseract.exe'
def image_extraction(request):
    if request.method == 'POST' and request.FILES['document']:
        document = request.FILES['document']

        # Convert uploaded file to an image
        try:
            img = Image.open(BytesIO(document.read()))
            text = pytesseract.image_to_string(img)
            
            extracted_data = ExtractedData.objects.create(
                document=document,
                extracted_text=text,
                document_type='image'
            )
            print("extracted_data",extracted_data)
            return render(request, 'result.html', {'extracted_data': extracted_data})
        except Exception as e:
            error_message = f"Error processing image: {e}"
            return render(request, 'error.html', {'error_message': error_message})
    
    return render(request, 'image_extraction.html')


def pdf_extraction(request):
    if request.method == 'POST' and request.FILES['document']:
        # Handle PDF extraction logic using PyPDF2
        # Save extracted text to database
        return render(request, 'result.html', {'extracted_text': extracted_text})

    return render(request, 'pdf_extraction.html')
