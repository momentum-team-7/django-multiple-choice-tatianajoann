from django.contrib import admin
from .models import User, Language, Snippet, Profile

# Register your models here.


admin.site.register(User)
admin.site.register(Language)
admin.site.register(Snippet)
admin.site.register(Profile)
