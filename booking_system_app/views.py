from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone
from djreservation.views import SimpleProductReservation
from .models import TableReservationSlot
from .forms import TableReservationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

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
    
@login_required(login_url='login')
def book_table(request):
    if request.method == "POST":
        form = TableReservationForm(request.POST)
        print("FORM ERRORS:", form.errors)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()

            send_mail(
                subject="Booking confirmation from The Wurst of Times",
                message=(
                    f"Hello {reservation.customer_name},\n\nYour reservation at The Wurst of Times has been confirmed:\n\n"
                    f"Table: {reservation.table.name} ({reservation.table.get_location_display()})\n"
                    f"When: {reservation.time_slot.strftime('%d-%m-%Y %H:%M')}\n"
                    f"Number of diners: {reservation.amount}\n"
                    f"Notes: {reservation.notes if reservation.notes else 'None'}\n\n"
                    f"We look forward to welcoming you!"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[request.user.email],
                fail_silently=False,
            )
            return redirect("reservation_success")
    else:
        form = TableReservationForm()

    return render(request, "booking_system_app/reservation_form.html", {"form": form})