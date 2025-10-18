from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.home, name="home"),
    path("menu/", views.menu, name="menu"),
    path("success/", views.reservation_success, name="reservation_success"),
    path("bookings/", views.book_table, name="book_table"),
]

