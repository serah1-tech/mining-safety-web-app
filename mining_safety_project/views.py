from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home(request):
    # Handle registration
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            login(request, user)  # Log the user in automatically
            return redirect('home')  # Redirect to the home page after successful registration
    else:
        form = UserCreationForm()  # Show empty form when the page loads

    # Additional context for other parts of the home page
    context = {
        'form': form,  # The registration form
        'education_content': 'Information about education programs related to mining safety.',
        'hazards_content': 'Details on various hazards and safety protocols in mining operations.',
        'other_content': 'Here is some additional content or a welcome message.',
    }

    return render(request, 'home.html', context)
