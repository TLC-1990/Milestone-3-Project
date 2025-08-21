from django.db import models
from django.contrib.auth.models import User
from django.db.models import ForeignKey
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.
#creating table name, location of table and number of seats
class Table(models.Model):
  name = models.CharField(max_length=30) 
  location = models.CharField(max_length=30, blank=True) 
  capacity = models.PositiveBigIntegerField()  
  
#creating time of reservation, number of guests in booking and table capacity 
class TableReservationSlot(models.Model):
  table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='slots')
  time_slot = models.DateTimeField()
  quantity = models.PositiveBigIntegerField(default=1)
  max_amount = models.PositiveBigIntegerField() 
  
#prevents the table from being booked again at the same time
class Meta:
        unique_together = ('table', 'time_slot')

def __str__(self):
  return f"{self.table.name} at {self.time_slot}"