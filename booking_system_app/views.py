from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone
from djreservation.views import SimpleProductReservation
from .models import TableReservationSlot
from .forms import TableReservationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def reservation_form(request):
    return render(request, "booking_system_app/reservation_form.html")

def home(request):
    return render(request, "booking_system_app/home.html")

def menu(request):
    return render(request, "booking_system_app/menu.html")

def table_reservations(request):
    return render(request, "booking_system_app/reservation_form.html")

def reservation_success(request):
    return render(request, "booking_system_app/reservation_success.html")


class TableReservation(SimpleProductReservation):
    base_model = TableReservationSlot
    amount_field = 'quantity'
    max_amount_field = 'max_amount'
    extra_display_field = ['table', 'time_slot']
    template_name = "booking_system_app/reservation_form.html"
    form_class = TableReservationForm 