from django.db import models
from django.contrib.auth.models import User
from django.db.models import ForeignKey
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta

# Create your models here.

MAX_TABLES_PER_LOCATION = {
  'inside' : 5,
  'outside' : 5,
} 
#creating table name, location of table and number of seats
class Table(models.Model):
  LOCATION_CHOICES = [
    ('inside', 'Inside'),
    ('outside', 'Outside')
  ]
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=10, choices=LOCATION_CHOICES)
  capacity = models.PositiveBigIntegerField()
  
  def __str__(self):
   return f"{self.name} ({self.get_location_display()}, capacity {self.capacity})"

#creating time of reservation, number of guests in booking, availability and table capacity 
class TableReservationSlot(models.Model):
  table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='slots')
  time_slot = models.DateTimeField()
  amount = models.PositiveBigIntegerField(default=1)
  available = models.BooleanField(default=True)
  available_amount = models.PositiveBigIntegerField(default=0)
  max_amount = models.PositiveBigIntegerField()
  notes = models.TextField(blank=True, null=True)
  
  
#prevents the table from being booked again at the same time
  class Meta:
        unique_together = ('table', 'time_slot')
  def clean(self):
        super().clean()

        
        location = self.table.location 
        
        existing_bookings = TableReservationSlot.objects.filter(
          table__location=location,
          time_slot=self.time_slot
        ).exclude(pk=self.pk).count()
        
        if existing_bookings >= MAX_TABLES_PER_LOCATION[location]:
          raise ValidationError(
            f"Sorry! All {MAX_TABLES_PER_LOCATION[location]} {location} tables are already booked for this time. Please pick a different time or location."
          )
  #creates alias for 'amount', so templates and codes can use 'num_people'
  @property
  def num_people(self):
    return self.amount
    
    
  @num_people.setter
  def num_people(self, value):
    self.amount = value
    
  @property
  def available_amount(self):
    return max(self.max_amount - self.amount, 0)
  
  
  def __str__(self):
     return (
       f"{self.table.name} ({self.table.get_location_display()},"
       f"capacity {self.table.capacity}) at {self.time_slot} "
       f"for {self.num_people} people"
     )


