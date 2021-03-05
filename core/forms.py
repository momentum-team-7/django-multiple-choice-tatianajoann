from django import forms
from .models import Language, Snippet


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name']


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['type_of', 'language', 'code']