from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from panel.models import Server

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
class LoginForm(RegisterForm):
    pass
class addServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = ["ip", 'password', "port"]