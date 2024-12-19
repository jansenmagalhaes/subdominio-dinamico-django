from django import forms
from django.contrib.auth import login, authenticate
from usuarios.models import Usuario

class AcessoForm(forms.Form):
    email = forms.EmailField(
        max_length = 254,
    )

    password = forms.CharField(
        strip = False,
    )

    def clean_email(self):
        data = self.cleaned_data.get('email')

        usuario = Usuario

        if not usuario.objects.filter(email=data).first():
            self.add_error('email', 'E-mail não cadastrado.')
        else:
            return data

    def clean_password(self):
        password = self.cleaned_data.get('password')

        usuario = Usuario

        self.user = authenticate(email=self.data.get('email'), password=password)

        if usuario.objects.filter(email=self.data.get('email')).first():
            if not self.user:
                self.add_error('password', 'Senha não confere.')
            else:
                if not self.user.ativo:
                    self.add_error('password', 'Usuário inativo. Verifique e-mail para ativação.')
                else:
                    return password
        else:
            self.add_error('password', 'Dados não cadastrados.')
    
    def log_into(self, request):
        login(request, self.user)