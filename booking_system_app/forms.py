from django import forms
from .models import TableReservationSlot
from django.forms.widgets import DateInput
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
    customer_name = forms.CharField(
        label="Your Name",
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your full name"
        })
    )
    date=forms.DateField(
        widget=DateInput(attrs={
            "class": "form-control",
            "id": "datepicker"
            }
        ),
        input_formats=["%d-%m-%Y"],
        label="Reservation Date"
    )
    time=forms.ChoiceField(choices=TIME_SLOTS, label="Time slot")
    
    amount = forms.ChoiceField(
        label="Number of Guests",
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.Select(attrs={"class":"form-control"})
    )
    
    notes = forms.CharField(
        label="Additonal Notes (allergies, special occasions or requests)",
        required=False,
        widget=forms.Textarea(attrs={"rows":3, "class":"form-control"})
    )
    
    email = forms.EmailField(
        label="Your Email",
        required=True,
        widget=forms.EmailInput(attrs={"class":"form-control",
                "placeholder": "Your email",
                "autocomplete":"email"
                })
    )
    available_amount = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = TableReservationSlot
        fields = ["customer_name", "table", "date", "time", "amount", "notes", "email"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            max_amount = getattr(self.instance, "max_amount", 0) or 0
            amount = getattr(self.instance, "amount", 0) or 0
            self.fields["available_amount"].initial = max(max_amount - amount, 0)
            
    def clean_date(self):
      selected_date = self.cleaned_data['date']
      if selected_date < date.today():
        raise forms.ValidationError("You cannot book a table in the past!")
      return selected_date
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        selected_date = self.cleaned_data["date"]
        selected_time = self.cleaned_data["time"]
        instance.time_slot = datetime.strptime(selected_time, "%H:%M").time()
        instance.date = selected_date
        instance.amount = int(self.cleaned_data["amount"])
        
        if commit:
            instance.save()
        return instance
    
