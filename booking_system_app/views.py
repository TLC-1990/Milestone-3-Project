from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone
from djreservation.views import SimpleProductReservation
from .models import TableReservationSlot

# Create your views here.
def home(request):
    return render(request, "booking_system_app/home.html")

def menu(request):
    return render(request, "booking_system_app/menu.html")

def table_reservations(request):
    return render(request, "booking_system_app/reservation_form.html")


class TableReservation(SimpleProductReservation):
    base_model = TableReservationSlot
    amount_field = 'quantity'       
    max_amount_field = 'max_amount' 
    extra_display_field = ['table', 'time_slot']
    template_name = "booking_system_app/reservation_form.html"