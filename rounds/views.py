from django.shortcuts import render, redirect
from .forms import RoundForm

# Create your views here.
def start_round(request):
    if request.method == 'POST':
        form = RoundForm(request.POST)

        if form.is_valid():
            round = form.save(commit=False)
            round.user = request.user
            round.save()

            return redirect('round_detail', round_id=round.id)

    else:
        form = RoundForm()
    
    return render(request, 'rounds/start_round.html', {
        'form': form
    })

def round_history(request):
    return render(request, 'rounds/round_history.html')