from django.urls import path
from . import views

urlpatterns = [
    path('menus/', views.menus_view, name='menus'),
]
