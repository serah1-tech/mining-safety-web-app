from django.shortcuts import render
from .models import SafetyLesson

def safety_lessons(request):
    lessons = SafetyLesson.objects.all()  # Fetch all safety lessons
    return render(request, 'safety_lessons.html', {'lessons': lessons})
