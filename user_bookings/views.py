from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from booking_system_app.models import TableReservationSlot
from booking_system_app.forms import TableReservationForm

# Create your views here.

@login_required
def booking_list(request):
    bookings = TableReservationSlot.objects.filter(user=request.user)
    return render(request, 'user_bookings/booking_list.html', {'bookings': bookings})

@login_required
def booking_edit(request, pk):
    booking = get_object_or_404(TableReservationSlot, pk=pk, user=request.user)