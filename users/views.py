from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Example: Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            messages.success(request, "Registration successful!")
            return redirect('home')  # Redirect to 'home' or another page
        else:
            messages.error(request, "There were errors in the form.")
    else:
        form = RegistrationForm()

    return render(request, 'home.html', {'form': form})
