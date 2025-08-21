from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone
from .models import AvailableHour, Reservation, is_slot_available
from .forms import ReservationForm

# Create your views here.


