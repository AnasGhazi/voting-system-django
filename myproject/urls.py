from django.urls import path, include
from django.contrib import admin  # Add this line
from django.views.generic import RedirectView

from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('register/', views.register_view, name='register'),  # Add this line for the registration page
    path('', RedirectView.as_view(url='accounts/login/', permanent=True)),  # Redirect root to login
     path('', include('polls.urls')),  # Include polls app URLs
]



