from django import forms
from django.contrib.auth import authenticate
from .models import Document, Document21
from .models import DiplomaDocument

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('documentName', 'documentName2', 'cycleType', 'studyGroup', 'teacherName', 'documentType', 'year', 'document')

class DocumentForm21(forms.ModelForm):
    class Meta:
        model = Document21
        fields = ('documentName21', 'docName21', 'cycleType21', 'studyGroup21', 'teacherName21', 'documentType21', 'year21', 'document21')

class DiplomaForm(forms.ModelForm):
    class Meta:
        model = DiplomaDocument
        fields = ('speciality', 'qualification', 'group','theme', 'student', 'year', 'document')