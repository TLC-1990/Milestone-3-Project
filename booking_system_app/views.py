from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone
from .models import AvailableHour, Reservation, is_slot_available
from .forms import ReservationForm

# Create your views here.

def create_reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            selected_hour = data['available_hour']
            requested_time = data['requested_time']
        
            if is_slot_available(selected_hour, requested_time.date()):
                Reservation.objects.create(
                    name=data['name'],
                    email=data['email'],
                    phone_number=data['phone_number'],
                    requested_time=requested_time,
                    available_hour=selected_hour,
                    other_notes=data.get('other_notes', '')
                )
                messages.success(request, 'Your reservation has been booked!')
                return redirect('reservation-success')
            else:
                messages.error(request, 'Sorry! That time slot is already booked, please choose another.')
    else:
        form = ReservationForm()

    return render(request, 'booking_system_app/reservation_form.html', {'form': form})
def index(request):
    return render(request, 'booking_system_app/index.html')    
def reservation_success(request):
    return render(request, 'booking_system_app/success.html')