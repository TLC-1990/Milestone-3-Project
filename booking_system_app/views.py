from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone
from djreservation.views import SimpleProductReservation
from .models import TableReservationSlot

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the booking system!")



class TableReservation(SimpleProductReservation):
    base_model = TableReservationSlot
    amount_field = 'quantity'       
    max_amount_field = 'max_amount' 
    extra_display_field = ['table', 'time_slot']