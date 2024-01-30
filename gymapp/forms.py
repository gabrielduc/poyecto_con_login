from django import forms
from .models import ClienteGimnasio

class ClienteGimnasioForm(forms.ModelForm):
    class Meta:
        model = ClienteGimnasio
        fields = ['nombre', 'apellido', 'rut', 'edad', 'genero', 'telefono', 'email']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)     

