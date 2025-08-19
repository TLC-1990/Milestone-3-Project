from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    requested_time = models.DateTimeField()
    other_notes = models.TextField(blank=True)
    
    def __str__(self):
      return f"{self.name} - {self.requested_time}"
  

        