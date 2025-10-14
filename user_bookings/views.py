from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from booking_system_app.models import TableReservationSlot
from booking_system_app.forms import TableReservationForm
from django.utils import timezone

# Create your views here.

@login_required
def booking_list(request):
    now = timezone.now()
    bookings = TableReservationSlot.objects.filter(user=request.user)
    past_bookings = bookings.filter(time_slot__lt=now).order_by('time_slot')
    future_bookings = bookings.filter(time_slot__gte=now).order_by('time_slot')
    return render(request, 'user_bookings/booking_list.html', {
        'past_bookings': past_bookings,
        'future_bookings': future_bookings,
        })

@login_required
def booking_edit(request, pk):
    booking = get_object_or_404(TableReservationSlot, pk=pk, user=request.user)
    if request.method=='POST':
        form = TableReservationForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('user_booking_list')
    else:
        form = TableReservationForm(instance=booking)
    return render(request, 'user_bookings/booking_edit.html', {'form': form})

@login_required
def booking_cancel(request, pk):
    booking = get_object_or_404(TableReservationSlot, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('user_booking_list')
    return render(request, 'user_bookings/booking_cancel_confirmation.html', { 'booking' : booking} )