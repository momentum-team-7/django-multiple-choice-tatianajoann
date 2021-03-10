from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from .models import Language, Snippet, User, Profile
from .forms import SnippetForm, LanguageForm, SearchForm
from django.http import HttpResponseRedirect, JsonResponse
import pyperclip

# Create your views here.

def superuser_only(function):


    def _inner(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied           
        return function(request, *args, **kwargs)
    return _inner


def homepage(request):
    languages = Language.objects.all()
    profiles = Profile.objects.all()
    form = SearchForm()
    return render(request, 'homepage.html', {'languages': languages, 'profiles':profiles, 'form': form})


def language_page(request, pk):
    language = get_object_or_404(Language, pk=pk)
    newlanguages = Language.objects.all()
    profiles = Profile.objects.all()
    snippets = Snippet.objects.filter(language=language)
    
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            term = form.cleaned_data["search"]
            languagesnip = snippets.filter(language__name__icontains=term)
            codesnip = snippets.filter(code__icontains=term)
            snippets = languagesnip | codesnip
    return render(request, 'language_page.html', {'language': language, 'snippets': snippets, 'newlanguages': newlanguages, 'form': form, 'profiles':profiles})


@login_required
def user_page(request, pk):
    languages = Language.objects.all()
    user = get_object_or_404(User, pk=pk)
    profiles = Profile.objects.all()
    snippets = Snippet.objects.filter(user=user)
    form = SearchForm()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            term = form.cleaned_data["search"]
            languagesnip = snippets.filter(language__name__icontains=term)
            codesnip = snippets.filter(code__icontains=term)
            snippets = languagesnip | codesnip
    return render(request, 'user_page.html', {'user': user, 'snippets': snippets, 'form': form, 'languages': languages, 'profiles': profiles})

@superuser_only
def all_users(request):
    users = User.objects.all()
    profiles = Profile.objects.all()
    return render(request, 'all_users.html', {'users': users, 'profiles': profiles})


def add_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect('/')
    else:
        form = SnippetForm()
    return render(request, 'add_snippet.html', {'form': form})


def save_snippet(request, pk):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        snippet = get_object_or_404(Snippet, pk=pk)
        user = request.user.username
        code = snippet.code
        language = snippet.language.name.lower()
        snippet.pk = None
        snippet.user = request.user
        snippet.save()
        pk = snippet.pk
        data = {
            'coppied': 'YES',
            'code':code,
            'language': language,
            'user': user,
            'pk': pk,
        }
    else:
        data = {
            'coppied': 'NO WAY'
        }
    return JsonResponse(data)


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
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        snippet = get_object_or_404(Snippet, pk=pk)
        snippet.delete()
        data = {
            'deleted': 'YES'
        }
    else:
        data = {
            'deleted': 'NO WAY'
        }
    return JsonResponse(data)


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
