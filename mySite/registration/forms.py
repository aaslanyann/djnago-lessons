from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class FormForCustomUser(ModelForm):
    phone_number = forms.CharField(max_length=30)
    class Meta:
        model = CustomUser
        fields = ["phone_number"]