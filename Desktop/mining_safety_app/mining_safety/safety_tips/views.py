from django.shortcuts import render
from .models import SafetyTip

def home(request):
    safety_tips = SafetyTip.objects.all()  # Get all safety tips
    return render(request, 'safety_tips/home.html', {'safety_tips': safety_tips})
