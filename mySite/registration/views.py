from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import RegistrationForm


def register(response):
    if response.method == 'POST':
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/polls')
    else:
        form = RegistrationForm()
    return render(response, 'registration/registration.html', {'form': form})