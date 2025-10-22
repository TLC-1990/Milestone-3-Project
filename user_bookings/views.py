"""Views for managing user bookings."""
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from booking_system_app.models import TableReservationSlot
from booking_system_app.forms import TableReservationForm
from django.utils import timezone
from datetime import date


@login_required
def booking_list(request):
    """Display the user's past and future bookings."""
    today = date.today()
    now_time = timezone.now().time()

    bookings = TableReservationSlot.objects.filter(email=request.user.email)

    past_bookings = bookings.filter(date__lt=today) | bookings.filter(
        date=today, time_slot__lt=now_time)
    past_bookings = past_bookings.order_by('date', 'time_slot')

    future_bookings = bookings.filter(date__gt=today) | bookings.filter(
        date=today, time_slot__gte=now_time)
    future_bookings = future_bookings.order_by('date', 'time_slot')

    return render(request, 'user_bookings/booking_list.html', {
        'past_bookings': past_bookings,
        'future_bookings': future_bookings,
    })


@login_required
def booking_edit(request, pk):
    """Edit an existing booking."""
    booking = get_object_or_404(TableReservationSlot,
                                pk=pk,
                                email=request.user.email)
    if request.method == 'POST':
        form = TableReservationForm(request.POST, instance=booking)
        if form.is_valid():
            try:
                form.save()
                return redirect('user_booking_list')
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = TableReservationForm(instance=booking)
    return render(request, 'user_bookings/booking_edit.html', {'form': form})


@login_required
def booking_cancel(request, pk):
    """Cancel an existing booking."""
    booking = get_object_or_404(TableReservationSlot, pk=pk,email=request.user.email)
    if request.method == 'POST':
        booking.delete()
        return redirect('user_booking_list')
    return render(request, 'user_bookings/booking_cancel_confirmation.html',
                  {'booking': booking})
