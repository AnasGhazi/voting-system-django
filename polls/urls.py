# polls/urls.py

from django.urls import path
from . import views

app_name = 'polls'  # This sets the application namespace

urlpatterns = [
    path('<int:poll_id>/vote/', views.vote_view, name='vote'),
    # Other URL patterns
]
