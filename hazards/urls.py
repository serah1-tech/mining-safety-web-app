from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hazards-home'),  # Home view
]
