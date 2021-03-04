from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Language, Snippet


# Create your views here.

@login_required
def homepage(request):
    languages = Language.objects.all()
    return render(request, 'homepage.html', {'languages': languages})


def language_page(request, pk):
    language = get_object_or_404(Language, pk=pk)
    snippets = Snippet.objects.filter(language=language)
    return render(request, 'language_page.html', {'language': language, 'snippets': snippets})


# def javascript_page(request, pk):
    languages = get_object_or_404(Language, pk=pk)
    return render(request, 'javascript_page.html', {'languages': languages})
