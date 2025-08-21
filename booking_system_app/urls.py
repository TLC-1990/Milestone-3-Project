from django.urls import path
from . import views
from .views import TableReservation

urlpatterns = [
    path("reservations/", TableReservation.as_view(), name="table_reservations"),
    path("", views.home, name="home"),
]