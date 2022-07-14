from django import forms
from . models import ShortURL

class ShortURLForm(forms.ModelForm):

    original_url = forms.CharField(label="Enter your long URL", 
        widget=forms.TextInput(attrs={'style' : 'width: 400px', 'placeholder': 'e.g. https://www.youtube.com/'}))
    alias = forms.CharField(max_length=7, label="https//:localhost:8000/", required=False) 

    class Meta:
        model = ShortURL
        fields = ['original_url']