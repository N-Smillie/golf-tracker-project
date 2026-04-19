from django.shortcuts import render

# Create your views here.
def start_round(request):
    return render(request, 'rounds/start_round.html')

def round_history(request):
    return render(request, 'rounds/round_history.html')