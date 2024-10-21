# rishtedaar/urls.py
from django.urls import path
from rishtedaar.views import health_check_view

urlpatterns = [
    path('health/', health_check_view, name='health_check'),
]
