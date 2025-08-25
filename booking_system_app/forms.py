from django import forms
from .models import TableReservationSlot
import datetime

DAYS_OF_THE_WEEK = [
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
    ('saturday', 'Saturday'),
    ('sunday', 'Sunday'),
]

TIME_SLOTS = [
    ("12:00", "12:00 PM"),
    ("12:30", "12:30 PM"),
    ("13:00", "1:30 PM"),
    ("13:30", "1:30 PM"),
    ("14:00", "2:00 PM"),
    ("14:30", "2:30 PM"),
    ("15:00", "3:00 PM"),
    ("15:30", "3:30 PM"),
    ("16:00", "4:00 PM"),
]

class TableReservationForm(forms.ModelForm):
    day=forms.ChoiceField(choices=DAYS_OF_THE_WEEK,label="Day of the week")
    time=forms.ChoiceField(choices=TIME_SLOTS, label="Time slot")
    
    
    class Meta:
        model = TableReservationSlot
        fields = ["table", "time_slot", "quantity"]
        
    def clean(self):
        cleaned_data = super().clean()