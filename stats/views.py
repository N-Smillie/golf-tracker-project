from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rounds.models import Round

# Create your views here.
def stats_dashboard(request):
    rounds = Round.objects.filter(user=request.user)

    full_rounds = []
    nine_rounds = []

    for round in rounds:
        scores = round.scores.all()

        total_strokes = 0
        total_par = 0

        for score in scores:
            total_strokes += score.strokes
            total_par += score.hole.par

        if total_strokes == 0:
            continue

        score_vs_par = total_strokes - total_par

        round.total_strokes = total_strokes
        round.total_par = total_par
        round.score_vs_par = score_vs_par

        # Separate into 9 or 18 hole rounds
        if round.holes_played == 'full18':
            full_rounds.append(round)
        else:
            nine_rounds.append(round)

        # Best round
        def get_best(rounds):
            if not rounds:
                return None

            best = rounds[0]

            for r in rounds:
                if r.score_vs_par < best.score_vs_par:
                    best = r

            return best
        
        # Worst round
        def get_worst(rounds):
            if not rounds:
                return None

            worst = rounds[0]

            for r in rounds:
                if r.score_vs_par > worst.score_vs_par:
                    worst = r

            return worst
        
        # Calculate average score vs par
        def get_average(rounds):
            if not rounds:
                return None

            total = 0

            for r in rounds:
                total += r.score_vs_par

            return total / len(rounds)
        
        best_full = get_best(full_rounds)
        worst_full = get_worst(full_rounds)
        avg_full = get_average(full_rounds)

        best_nine = get_best(nine_rounds)
        worst_nine = get_worst(nine_rounds)
        avg_nine = get_average(nine_rounds)

        context = {
        'best_full': best_full,
        'worst_full': worst_full,
        'avg_full': avg_full,

        'best_nine': best_nine,
        'worst_nine': worst_nine,
        'avg_nine': avg_nine,
    }
        
        return render(request, 'stats/stats_dashboard.html', context)
    