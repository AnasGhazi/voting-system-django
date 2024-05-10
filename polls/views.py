from django.shortcuts import render, redirect, get_object_or_404
from .models import Poll, Choice

from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from .models import Poll, Choice



def vote_view(request, poll_id):
    print("Received poll_id:", poll_id)  # Add this line for debugging
    poll = get_object_or_404(Poll, pk=poll_id)
    print("Retrieved poll:", poll)  # Add this line for debugging
    # Rest of the view code
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


def vote(request, poll_id):
    if request.method == 'POST':
        poll = get_object_or_404(Poll, pk=poll_id)
        choice_id = request.POST.get('choice')
        selected_choice = get_object_or_404(Choice, pk=choice_id)
        selected_choice.votes += 1
        selected_choice.save()
        # Optionally, you can add logic here to mark the selected choice as correct if needed
        return redirect('dashboard')
    else:
        return redirect('dashboard')  # Redirect if not a POST request

from django.shortcuts import render
from .models import Poll

def dashboard(request):
    # Fetch all polls with their choices
    polls = Poll.objects.all()
    context = {
        'polls': polls
    }
    return render(request, 'dashboard/dashboard.html', context)

