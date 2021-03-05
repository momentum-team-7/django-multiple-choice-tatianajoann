from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Language(models.Model):
    name = models.CharField(max_length=280)

    def __str__(self):
        return self.name


class Snippet(models.Model):
    type_of = models.CharField(max_length=280)
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, blank=True, null=True, related_name="language")
    code = models.CharField(max_length=1500, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='user')

    def __str__(self):
        return self.type_of
