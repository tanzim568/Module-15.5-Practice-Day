from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model=Album
        fields='__all__'
        
        widgets = {
            'release': forms.DateInput(attrs={'type':'date'}),
        }
        help_texts ={
            'name': "Write album name",
            'rating':'Choose a rating between 1 to 5'
        }
       