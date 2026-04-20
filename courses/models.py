from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    
class Hole(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='holes')
    number = models.IntegerField()
    par = models.IntegerField()

    def __str__(self):
        return f"{self.course.name} - Hole {self.number}"