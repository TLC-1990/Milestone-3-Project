from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="booking_home"),
    path("reserve/", views.create_reservation_view, name="create_reservation_view"), 
    path('success/', views.reservation_success, name='reservation_success'),
    path("reservation/form/", views.reservation_form, name="reservation_form"),
]
