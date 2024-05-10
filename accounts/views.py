from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Poll

# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect authenticated users to the dashboard
                return redirect('dashboard')  # Assuming the name of the dashboard URL is 'dashboard'
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def register_view(request):
    print("Register view called")  # Add debug statement to check if the function is being called

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Add debug statement to check if the form is valid
            user = form.save()
            print("User created:", user.username)  # Add debug statement to check if the user is created successfully
            # Redirect to the login page after registration
            return redirect('login')
        else:
            print("Form errors:", form.errors)  # Add debug statement to print form validation errors
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})

# accounts/views.py

from django.shortcuts import render
from polls.models import Choice, Poll  # Import the Poll model

# accounts/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Poll

def vote_view(request, poll_id):
    if request.method == 'POST':
        poll = get_object_or_404(Poll, pk=poll_id)
        choice_id = request.POST.get('choice')
        if choice_id is not None:
            selected_choice = get_object_or_404(Choice, pk=choice_id)
            selected_choice.votes += 1
            selected_choice.save()
            return redirect('dashboard')  # Redirect to the dashboard after voting
        else:
            return HttpResponse("Invalid form submission")
    else:
        return HttpResponse("Method not allowed")

def dashboard_view(request):
    # Retrieve all polls
    polls = Poll.objects.all()
    context = {
        'polls': polls
    }
    return render(request, 'dashboard/dashboard.html', context)

