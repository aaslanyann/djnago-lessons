from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=30)

    class Meta:
        model = CustomUser
        fields = ("email", 'phone_number')

