from django.urls import path
from .views import landing_render

urlpatterns = [
    path('', landing_render, name='landing'),
]