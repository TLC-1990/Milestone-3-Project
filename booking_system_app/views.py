from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone
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


@login_required(login_url='login')
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
            reservation.user = request.user
            reservation.save()

            # send confirmation email (do not block on failure)
            try:
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
            except Exception:
                print("Warning: failed to send booking confirmation email")

            return redirect("reservation_success")
        # else: fall through and re-render form with errors
    else:
        form = TableReservationForm(instance=slot)

    return render(request, "booking_system_app/reservation_form.html", {"form": form})

