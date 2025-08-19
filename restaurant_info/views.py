from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rest_info(request):
    return HttpResponse("This would be the restaurant information page!")