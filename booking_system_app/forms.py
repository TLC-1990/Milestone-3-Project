from django import forms
from .models import TableReservationSlot

class TableReservationForm(forms.ModelForm):
    class Meta:
        model = TableReservationSlot
        fields = ["table", "time_slot", "quantity"]