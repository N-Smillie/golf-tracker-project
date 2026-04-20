from django.db import models
from django.contrib.auth.models import User
from courses.models import Course, Hole

# Create your models here.
class Round(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    HOLE_CHOICES = [
        ('front9', 'Front 9'),
        ('back9', 'Back 9'),
        ('full18', 'Full 18'),
    ]
    holes_played = models.CharField(max_length=10, choices=HOLE_CHOICES)

    def __str__(self):
        return f"{self.user} - {self.course} ({self.date})"
    

class Score(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='scores')
    hole = models.ForeignKey(Hole, on_delete=models.CASCADE)
    strokes = models.IntegerField()

    def __str__(self):
        return f"Round {self.round.id} - Hole {self.hole.number}: {self.strokes}"