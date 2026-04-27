from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rounds.models import Round, Score
from django.db.models import Sum, Avg

# Create your views here.
@login_required
def stats_dashboard(request):
    rounds = Round.objects.filter(user=request.user)

    # Calculates the total strokes for each user's round
    rounds_with_totals = rounds.annotate(
        total_strokes=Sum('scores__strokes')
    )

    # Best round
    best_round = rounds_with_totals.order_by('total_strokes').first()

    # Worst round
    worst_round = rounds_with_totals.order_by('-total_strokes').first()

    # Calculates average score per round
    totals = [r.total_strokes for r in rounds_with_totals if r.total_strokes]

    if totals:
        average_score = sum(totals) / len(totals)
    else:
        average_score = None

    context = {
        'rounds': rounds_with_totals,
        'best_round': best_round,
        'worst_round': worst_round,
        'average_score': average_score,
    }

    return render(request, 'stats/stats_dashboard.html', context)