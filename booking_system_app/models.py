from django.db import models
from django.contrib.auth.models import User
from django.db.models import ForeignKey
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.
DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
     ) 

class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    requested_time = models.DateTimeField()
    available_hour = models.ForeignKey(
      'AvailableHour', 
      on_delete=models.CASCADE,
      related_name="reservations",
      null=True,
      blank=True
    )
    other_notes = models.TextField(blank=True)
    
    def __str__(self):
      return f"{self.name} - {self.requested_time}" 
  
    
class WeekDay(models.Model):
    restaurant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="weekdays"
    )
    day = models.IntegerField(choices=DAYS_OF_WEEK)
    
    def __str__(self):
        return f"{self.get_day_display()} - {self.restaurant.username}"
# timeslot
class AvailableHour(models.Model): #Based on weekday
    weekday = models.ForeignKey(
        WeekDay,
        on_delete=models.CASCADE,
        related_name="available_hours"
    )
    from_hour = models.TimeField()
    to_hour = models.TimeField()
    booked_by = ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f"{self.weekday}: {self.from_hour} to {self.to_hour}"

# Utility function to check if slot is already booked 
def is_slot_available(available_hour, date):
    existing = Reservation.objects.filter(
        requested_time__date=date,
        available_hour=available_hour
    ).exists()
    return not existing 
  
           