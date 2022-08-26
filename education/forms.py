from pyexpat import model
from django import forms  
from .models import imag

class UploadForm(forms.Form):
    # class meta:
    #     model = imag
    #     fields = "__all__"
    file=forms.FileField()