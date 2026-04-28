from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rounds.models import Round, Score


@login_required
def stats_dashboard(request):
    rounds = Round.objects.filter(user=request.user)

    full_rounds = []
    nine_rounds = []
    valid_rounds = []

    for round in rounds:
        scores = round.scores.all()

        if not scores.exists():
            continue

        total_strokes = 0
        total_par = 0

        for score in scores:
            total_strokes += score.strokes
            total_par += score.hole.par

        round.total_strokes = total_strokes
        round.total_par = total_par
        round.score_vs_par = total_strokes - total_par

        valid_rounds.append(round)


        # Separate into 9/18 holes

        if round.holes_played == 'full18':
            full_rounds.append(round)
        else:
            nine_rounds.append(round)

    # Best Round
    def get_best(round_list):
        if not round_list:
            return None

        best = round_list[0]
        for r in round_list:
            if r.score_vs_par < best.score_vs_par:
                best = r
        return best

    # Worst Round
    def get_worst(round_list):
        if not round_list:
            return None

        worst = round_list[0]
        for r in round_list:
            if r.score_vs_par > worst.score_vs_par:
                worst = r
        return worst

    best_full = get_best(full_rounds)
    worst_full = get_worst(full_rounds)

    best_nine = get_best(nine_rounds)
    worst_nine = get_worst(nine_rounds)


    # Calculate average
    def get_average(round_list):
        if not round_list:
            return None

        total = 0
        for r in round_list:
            total += r.score_vs_par

        return total / len(round_list)

    avg_full = get_average(full_rounds)
    avg_nine = get_average(nine_rounds)

   
    # Context
    context = {
        'rounds': valid_rounds,

        'best_full': best_full,
        'worst_full': worst_full,
        'avg_full': avg_full,

        'best_nine': best_nine,
        'worst_nine': worst_nine,
        'avg_nine': avg_nine,
    }

    return render(request, 'stats/stats_dashboard.html', context)
    