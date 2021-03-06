from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Language, Snippet, User
from .forms import SnippetForm, LanguageForm, SearchForm
from django.http import HttpResponseRedirect
import pyperclip

# Create your views here.


def homepage(request):
    languages = Language.objects.all()
    return render(request, 'homepage.html', {'languages': languages})


def language_page(request, pk):
    language = get_object_or_404(Language, pk=pk)
    snippets = Snippet.objects.filter(language=language)
    return render(request, 'language_page.html', {'language': language, 'snippets': snippets})


@login_required
def user_page(request, pk):
    user = get_object_or_404(User, pk=pk)
    snippets = Snippet.objects.filter(user=user)
    form = SearchForm()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            term = form.cleaned_data["search"]
            snippets = snippets.filter(language__name__icontains=term)
    return render(request, 'user_page.html', {'user': user, 'snippets': snippets, 'form': form})


def add_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = SnippetForm()
    return render(request, 'add_snippet.html', {'form': form})


def edit_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'edit_snippet.html', {'form': form, 'snippet': snippet})


def delete_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    snippet.delete()
    return HttpResponseRedirect('/')


def copy_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    pyperclip.copy(snippet.code)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add_language(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = LanguageForm()
    return render(request, 'add_language.html', {'form': form})

# we might not need this or the add language but I figured I'd just put them down really quick in case we do want them & we can take them out later if not


def edit_language(request, pk):
    language = get_object_or_404(Language, pk=pk)
    if request.method == 'POST':
        form = LanguageForm(request.POST, instance=language)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = LanguageForm(instance=language)
    return render(request, 'edit_language.html', {'form': form, 'language': language})


# class search_results(ListView):
#     template_name='search_results.html'

#     def results(self):

#         return Snippet.objects.filter(name__icontains='python')
