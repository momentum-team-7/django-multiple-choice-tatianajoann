from django import forms
from .models import Language, Snippet, Profile
from django.forms import ClearableFileInput


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name']


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['type_of', 'language', 'code']


class SearchForm(forms.Form):
    search = forms.CharField(label="search", max_length=80)


class UploadFileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image']






