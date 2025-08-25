from django.urls import path
from . import views
from .views import home, menu, TableReservation, reservation_success


urlpatterns = [
    path("home/", views.home, name="home"),
    path("menu/", views.menu, name="menu"),
    path("success/", reservation_success, name="reservation_success"),
    path("<int:pk>/", TableReservation.as_view(), name="table_reservation"),
]