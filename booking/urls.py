from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('booking/', views.booking, name='booking'),
    path('cancel/', views.cancel, name='cancel'),
    path('availability/', views.availability, name='availability'),
]