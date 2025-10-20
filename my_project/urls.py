from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from booking_system_app import views as booking_views




urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('my-bookings/', include('user_bookings.urls')),
    
    path("", lambda request: redirect("home/")),
    path("menu/", booking_views.menu, name="menu"),
    
    path("", include("booking_system_app.urls")),
]