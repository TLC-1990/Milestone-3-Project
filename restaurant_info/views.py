from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def menus_view(request):
    return render(request, 'restaurant_info/menus.html')