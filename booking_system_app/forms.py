from django import forms
from .models import Reservation, AvailableHour

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone_number', 'requested_time', 'available_hour', 'other_notes']
        widgets = {
            'requested_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }