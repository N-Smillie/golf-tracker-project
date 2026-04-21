from django.shortcuts import render, redirect, get_object_or_404
from .forms import RoundForm
from .models import Round, Score
from courses.models import Hole


def start_round(request):
    if request.method == 'POST':
        form = RoundForm(request.POST)

        if form.is_valid():
            round = form.save(commit=False)
            round.user = request.user
            round.save()

            # Redirect to round detail page after creation
            return redirect('round_detail', round_id=round.id)

    else:
        form = RoundForm()

    return render(request, 'rounds/start_round.html', {
        'form': form
    })


def round_history(request):
    # Show only the logged-in user's rounds
    rounds = Round.objects.filter(user=request.user).order_by('-date')

    return render(request, 'rounds/round_history.html', {
        'rounds': rounds
    })


def round_detail(request, round_id):
    round = get_object_or_404(Round, id=round_id)

    # Determine which holes to show
    if round.holes_played == 'front9':
        holes = round.course.holes.all()[:9]
    elif round.holes_played == 'back9':
        holes = round.course.holes.all()[9:]
    else:
        holes = round.course.holes.all()

    if request.method == 'POST':
        for hole in holes:
            strokes = request.POST.get(f'hole_{hole.id}')

            if strokes:
                Score.objects.update_or_create(
                    round=round,
                    hole=hole,
                    defaults={'strokes': strokes}
                )

        return redirect('round_detail', round_id=round.id)

    return render(request, 'rounds/round_detail.html', {
        'round': round,
        'holes': holes
    })