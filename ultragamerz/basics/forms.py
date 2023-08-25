from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import message

class RegisterForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    class Meta:
        model=User
        fields=["username","email","first_name","last_name","password1","password2"]


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class messageForm(forms.ModelForm):
    class Meta:
        model=message
        fields=["name","email","message"]