from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrarUsuarioForm(UserCreationForm):
    username = forms.CharField(label="Username", max_length=50)
    first_name= forms.CharField(label="Nombre", max_length=50)
    last_name= forms.CharField(label="Apellido", max_length=50)
    email = forms.EmailField(label="Email ")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)
    

    class Meta:
        model= User
        fields =  ["username", "first_name", "last_name" ,"email", "password1", "password2"]
        help_texts = {k:"" for k in fields}




class EditarPerfilForm(UserCreationForm):
    
    first_name= forms.CharField(label="Nombre", max_length=50)
    last_name= forms.CharField(label="Apellido", max_length=50)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)
    

    class Meta:
        model= User
        fields =  ["first_name", "last_name","email", "password1", "password2" ]
        help_texts = {k:"" for k in fields}