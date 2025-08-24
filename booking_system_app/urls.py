from django.urls import path
from . import views
from .views import TableReservation


urlpatterns = [
    path("", views.home, name="home"),
    path("menu/", views.menu, name="menu"),
    path("reservations/success/", views.reservation_success, name="reservation_success"),
    path("reservations/", TableReservation.as_view(), name="table_reservations"),
    
    path("reservations/<int:pk>/", TableReservation.as_view(), name="table_reservation"),
]