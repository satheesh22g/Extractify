# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('image-extraction/', views.image_extraction, name='image_extraction'),
    path('pdf-extraction/', views.pdf_extraction, name='pdf_extraction'),
    # Other URLs within your app if needed
]
