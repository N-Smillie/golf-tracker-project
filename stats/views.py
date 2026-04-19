from django.shortcuts import render

# Create your views here.
def stats_dashboard(request):
    return render(request, 'stats/stats_dashboard.html')