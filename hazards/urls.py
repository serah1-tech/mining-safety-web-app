# In your app's urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hazards/', views.hazards, name='hazards'),
]
