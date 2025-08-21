from django.urls import path
from . import views
from .views import TableReservation

urlpatterns = [
    path('', views.index, name="booking_home"),
    path("reservations/", TableReservation.as_view(), name="table_reservations"),
]