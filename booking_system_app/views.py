from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.core.mail import send_mail
from .models import TableReservationSlot
from .forms import TableReservationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings

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

@login_required(login_url='account_login')
def book_table(request, pk=None):
    """Handle booking form; optional `pk` binds the form to a TableReservationSlot instance."""
    slot = None
    if pk is not None:
        slot = get_object_or_404(TableReservationSlot, pk=pk)

    if request.method == "POST":
        form = TableReservationForm(request.POST, instance=slot)
        print("FORM ERRORS:", form.errors)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.email = request.user.email
            reservation.save()
            
            return redirect("reservation_success")
    else:
        if slot is not None:
            form = TableReservationForm(instance=slot)
        else:
            form = TableReservationForm(initial={
                "email": request.user.email,
            })
    return render(request, "booking_system_app/reservation_form.html", {"form": form})

