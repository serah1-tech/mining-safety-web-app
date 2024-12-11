
from .models import Lesson  # Ensure you have a 'Lesson' model
from django.shortcuts import render

def safety_lessons(request):
    # You can pass data to the template if needed
    return render(request, 'education/safety_lessons.html')



def home(request):
    return render(request, 'home.html')
