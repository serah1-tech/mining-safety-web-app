from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # This ensures the 'register' name is correct
]
