from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Language, Snippet


# Create your views here.

@login_required
def homepage(request):
    return render(request, 'homepage.html', {})


