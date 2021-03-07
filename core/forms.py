from django import forms
from .models import Language, Snippet, User


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name']


class SnippetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SnippetForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True
        self.fields['user'].widget = forms.HiddenInput()

    class Meta:
        model = Snippet
        fields = ['type_of', 'language', 'code', 'user']


class SearchForm(forms.Form):
    search = forms.CharField(label="search", max_length=80)
