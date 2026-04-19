from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start_round, name='start_round'),
    path('history/', views.round_history, name='round_history'),
]