from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.urls import reverse 
from django.contrib.auth.views import LoginView
# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    
    def get_success_url(self):
        return reverse("table_reservation", kwargs={"pk":self.request.user.pk})