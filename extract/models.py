from django.db import models

class ExtractedData(models.Model):
    document = models.FileField(upload_to='documents/')
    extracted_text = models.TextField()
    document_type = models.CharField(max_length=10)  # 'image' or 'pdf'
