from django import forms
from .models import Bookmark

class BookmarkForm(forms.ModelForm):

  class Meta:
    model = Bookmark
    fields = ( 'name', 'url', 'notes' )
    widgets = {
        'name': forms.TextInput(attrs={'placeholder': 'e.g. Example Website'}),
        'url': forms.TextInput(attrs={'placeholder': 'e.g. https://www.example.com'}),
        'notes': forms.Textarea(attrs={'placeholder': ''}),
    }
