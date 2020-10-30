from django import forms
from django.contrib.auth import authenticate
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('documentName', 'documentName2', 'teacherName', 'documentType', 'document')