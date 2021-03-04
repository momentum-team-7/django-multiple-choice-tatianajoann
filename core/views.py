from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Language, Snippet


# Create your views here.

@login_required
def homepage(request):
    return render(request, 'homepage.html', {})


def python_page(request):
    languages = Language.objects.all()
    return render(request, 'python_page.html', {'languages': languages})


def javascript_page(request):
    languages = Language.objects.all()
    return render(request, 'javascript_page.html', {'languages': languages})