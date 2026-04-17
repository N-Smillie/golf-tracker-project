from django.shortcuts import render

# Create your views here.
def start_round(request):
    return render(request, 'rounds/start_round.html')