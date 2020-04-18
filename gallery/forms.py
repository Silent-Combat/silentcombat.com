from django import forms

class ImageUpload(forms.Form):
    name = forms.CharField(max_length=50)
    path = forms.FileField()