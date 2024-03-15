from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import RegistrationForm, FormForCustomUser
from .models import CustomUser

def register(response):
    if response.method == 'POST':
        form = RegistrationForm(response.POST)
        custom_form = FormForCustomUser(response.POST)
        if form.is_valid() and custom_form.is_valid():
            createdUser = form.save()
            custom_user = CustomUser(user=createdUser, phone_number=response.POST.get('phone_number'))
            custom_user.save()
            return redirect('/polls')
    else:
        form = RegistrationForm()
        custom_form = FormForCustomUser()
    return render(response, 'registration/registration.html', {'form': form, 'custom_form': custom_form})