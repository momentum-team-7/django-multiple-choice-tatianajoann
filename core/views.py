from django.shortcuts import render
from .models import Language, Snippet


# Create your views here.


def homepage(request):
    return render(request, 'homepage.html', {})


