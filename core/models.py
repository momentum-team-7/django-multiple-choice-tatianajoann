from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Profile(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    bio = models.TextField(max_length=350, blank=True, null=True)


class Language(models.Model):
    name = models.CharField(max_length=280)

    def __str__(self):
        return self.name


class Snippet(models.Model):
    type_of = models.CharField(max_length=280)
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, blank=True, null=True, related_name="language")
    code = models.TextField(max_length=1500, blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, related_name='user')

    def __str__(self):
        return f'{self.code},{self.type_of}'
