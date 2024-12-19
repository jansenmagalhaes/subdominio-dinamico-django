from django.contrib import admin
from django.contrib.auth import admin as admin_auth_django
from .models import Usuario
from .forms import UserCreationForm, UserChangeForm

@admin.register(Usuario)
class UserAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Usuario
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ("Organização", {"fields": ("organizacao",)}),
    )