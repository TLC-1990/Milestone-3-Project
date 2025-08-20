from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm 
from .google_sheets import append_customer_to_sheet
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            form.save() 
            append_customer_to_sheet(first_name, last_name, email, password)
            messages.success(request, f'Account created for {email}!') 
            return redirect('booking') 
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})