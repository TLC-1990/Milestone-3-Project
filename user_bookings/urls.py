from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_list, name='user_booking_list'),
    path('<int:pk>/edit/', views.booking_edit, name='user_booking_edit'),
]