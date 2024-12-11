# In your app's views.py
from django.shortcuts import render

def hazards(request):
    return render(request, 'hazards/alert_list.html')  # Correct path to the template
