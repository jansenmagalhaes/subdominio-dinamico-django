from django import forms
from django.contrib.auth import forms as formsAuth
from .models import Usuario

class UserCreationForm(formsAuth.UserCreationForm):
    class Meta(formsAuth.UserCreationForm.Meta):
        model = Usuario

class UserChangeForm(formsAuth.UserChangeForm):
    class Meta(formsAuth.UserChangeForm.Meta):
        model = Usuario
