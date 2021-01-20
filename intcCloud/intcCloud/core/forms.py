from django import forms
from django.contrib.auth import authenticate
from .models import Document
from .models import DiplomaDocument

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('documentName', 'documentName2', 'cycleType', 'studyGroup', 'teacherName', 'documentType', 'document')

class DiplomaForm(forms.ModelForm):
    class Meta:
        model = DiplomaDocument
        fields = ('speciality', 'qualification', 'group','theme', 'student', 'document')