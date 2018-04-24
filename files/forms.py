from django import forms
from .models import File

class FileForm(forms.ModelForm):

  class Meta:
    model = File
    fields = ( 'name', 'upload' )
    widgets = {
        'name': forms.TextInput(attrs={'placeholder': 'e.g. My Resume'}),
        'upload': forms.FileInput(),
    }
