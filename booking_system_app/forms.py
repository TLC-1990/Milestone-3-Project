from django import forms
from .models import TableReservationSlot
from bootstrap_datepicker_plus.widgets import DatePickerInput
from datetime import date, datetime
from django.core.validators import MaxValueValidator


TIME_SLOTS = [
    ("12:00", "12:00 PM"),
    ("12:30", "12:30 PM"),
    ("13:00", "1:00 PM"),
    ("13:30", "1:30 PM"),
    ("14:00", "2:00 PM"),
    ("14:30", "2:30 PM"),
    ("15:00", "3:00 PM"),
    ("15:30", "3:30 PM"),
    ("16:00", "4:00 PM"),
]

class TableReservationForm(forms.ModelForm):
    date=forms.DateField(
        widget=DatePickerInput(
            options={
                "format": "DD-MM-YYYY",
                "minDate":str(date.today()),
                "showClose": True,
                "showClear": True,
                "showTodayButton":True,
            }
        ),
        label="Reservation Date"
    )
    time=forms.ChoiceField(choices=TIME_SLOTS, label="Time slot")
    
    amount = forms.ChoiceField(
        label="Number of Guests",
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.NumberInput(attrs={"class":"form-control"})
    )
    
    notes = forms.CharField(
        label="Additonal Notes (allergies, special occasions or requests)",
        required=False,
        widget=forms.Textarea(attrs={"rows":3, "class":"form-control"})
    )
    
    email = forms.EmailField(
        label="Your Email",
        required=True,
        widget=forms.EmailInput(attrs={"class":"form-control"})
    )
    class Meta:
        model = TableReservationSlot
        fields = ["table", "date", "time", "notes", "email"]
        
    def clean_date(self):
      selected_date = self.cleaned_data['date']
      if selected_date < date.today():
        raise forms.ValidationError("You cannot book a table in the past!")
      return selected_date
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        selected_date = self.cleaned_data["date"]
        selected_time = self.cleaned_data["time"]
        instance.time_slot = datetime.strptime(
            f"{selected_date} {selected_time}", "%Y-%m-%d %H:%M"
        )
        
        if commit:
            instance.save()
        return instance