from django.urls import path
from . import views

urlpatterns = [
    path('', views.stats_dashboard, name='stats_dashboard'),
]