from django.contrib import admin
from .models import Course, Hole

# Register your models here.

class HoleInline(admin.TabularInline):
    model = Hole
    extra = 0
    ordering = ('number',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [HoleInline]

@admin.register(Hole)
class HoleAdmin(admin.ModelAdmin):
    list_display = ('course', 'number', 'par')
    list_filter = ('course',)
    ordering = ('course', 'number')