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
    
    # Get existing scores
    scores = {score.hole.id: score.strokes
              for score in Score.objects.filter(round=round)}

    # Give score to each hole
    total_strokes = 0
    total_par = 0
    running_score = 0

    for hole in holes:
        hole.score = scores.get(hole.id)

        total_par += hole.par

        if hole.score:
            hole.score = int(hole.score)
            total_strokes += int(hole.score)

            # Calculation for difference between score and par
            hole.diff = hole.score - hole.par

            # Running Total
            running_score += hole.diff
            hole.running_total = running_score

            # Determine result (birdie/bogey etc)
            if hole.diff == -3:
                hole.result = "Albatross"
            elif hole.diff == -2:
                hole.result = "Eagle"
            elif hole.diff == -1:
                hole.result = "Birdie"
            elif hole.diff == 0:
                hole.result = "Par"
            elif hole.diff == 1:
                hole.result = "Bogey"
            elif hole.diff == 2:
                hole.result = "Double Bogey"
            elif hole.diff == 3:
                hole.result = "Triple Bogey"
            else:
                hole.result = f"{hole.diff:+}"
        else:
            hole.diff = None
            hole.result = ""
            hole.running_total = None
            

    # Calculation for over/under par
    score_vs_par = total_strokes - total_par

    return render(request, 'rounds/round_detail.html', {
        'round': round,
        'holes': holes,
        'total_strokes': total_strokes,
        'total_par': total_par,
        'score_vs_par': score_vs_par,
    })