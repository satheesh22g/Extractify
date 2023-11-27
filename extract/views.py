from django.shortcuts import render
from .models import ExtractedData
import pytesseract
from PIL import Image
from io import BytesIO
pytesseract.pytesseract.tesseract_cmd = r'G:\tessaract\tesseract.exe'

def home(request):
    return render(request, 'home.html')
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


import PyPDF2
from django.shortcuts import render

def pdf_extraction(request):
    if request.method == 'POST' and request.FILES['document']:
        uploaded_file = request.FILES['document']
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        extracted_text = ''

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            extracted_text += page.extract_text()
        extracted_text = extracted_text.replace('\n', ' ')
        document_type = 'PDF'  # You can set the document type as needed
        pdf_url = uploaded_file.url if hasattr(uploaded_file, 'url') else None
        # Create a dictionary with extracted text and document type
        extracted_data = {
            'extracted_text': extracted_text,
            'document_type': document_type,
            'pdf_url' : pdf_url
        }

        return render(request, 'result.html', {'extracted_data': extracted_data})

    return render(request, 'pdf_extraction.html')