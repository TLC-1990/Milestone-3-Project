from django.urls import path
from . import views
from .views import TableReservation


urlpatterns = [
    path("", views.table_reservations, name="table_reservations"),
    path("reservations/<int:pk>/", TableReservation.as_view(), name="table_reservation"),
    path("menu/", views.menu, name="menu"),
]