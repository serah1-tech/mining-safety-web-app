from django.urls import path
from . import views

urlpatterns = [
    path('safety_lessons/', views.safety_lessons, name='safety_lessons'),  # Use a specific name for the view
]

