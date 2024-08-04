from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)  # in cm
    fitness_level = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ], default='beginner')

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField(blank=True)

class Program(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class WorkoutDay(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    day_number = models.IntegerField()

class ProgramExercise(models.Model):
    workout_day = models.ForeignKey(WorkoutDay, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField()
    reps = models.IntegerField()
    target_weight = models.FloatField()

class Workout(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    is_completed = models.BooleanField(default=False)
    is_partial = models.BooleanField(default=False)
    comments = models.TextField(blank=True)

class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    planned_sets = models.IntegerField()
    planned_reps = models.IntegerField()
    planned_weight = models.FloatField()
    actual_sets = models.IntegerField(null=True, blank=True)
    actual_reps = models.IntegerField(null=True, blank=True)
    actual_weight = models.FloatField(null=True, blank=True)
    is_skipped = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

class BodyWeightLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField()
