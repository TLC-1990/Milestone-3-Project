from django import forms
from .models import TableReservationSlot
from bootstrap_datepicker_plus.widgets import DatePickerInput
from datetime import date, datetime


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
    
    num_people = forms.IntegerField(
        label="Number of guests",
        min_value=1,
        widget=forms.NumberInput(attrs={"class":"form-control"})

    )
    class Meta:
        model = TableReservationSlot
        fields = ["table", "date", "time", "num_people"]
        
    def clean(self):
        cleaned_data = super().clean()
        
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
        
        instance.amount = self.cleaned_data["num_people"]
        
        if commit:
            instance.save()
        return instance