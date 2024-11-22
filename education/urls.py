from django.urls import path
from .views import safety_lessons

urlpatterns = [
    path('lessons/', safety_lessons, name='safety_lessons'),  # Added this line
]
