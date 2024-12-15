from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Registration URL in users app
]
