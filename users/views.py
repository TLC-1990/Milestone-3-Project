from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm 
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            form.save() 
            from django.contrib.auth import login
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created for {email}!') 
            return render(request, 'users/regsuccess.html', {'email': email})
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})