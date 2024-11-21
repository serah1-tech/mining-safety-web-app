from django.urls import path
from . import views

# Define the URL patterns for this app
urlpatterns = [
    path('', views.home, name='home'),  # Home page route
]
