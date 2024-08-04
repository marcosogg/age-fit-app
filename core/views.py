from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import CustomUser, Exercise, Program, WorkoutDay, ProgramExercise, Workout, WorkoutExercise, BodyWeightLog
from .serializers import CustomUserSerializer, ExerciseSerializer, ProgramSerializer, WorkoutDaySerializer, ProgramExerciseSerializer, WorkoutSerializer, WorkoutExerciseSerializer, BodyWeightLogSerializer

def home(request):
    return HttpResponse("<h1>Welcome to Age Fit App</h1>")

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class WorkoutDayViewSet(viewsets.ModelViewSet):
    queryset = WorkoutDay.objects.all()
    serializer_class = WorkoutDaySerializer

class ProgramExerciseViewSet(viewsets.ModelViewSet):
    queryset = ProgramExercise.objects.all()
    serializer_class = ProgramExerciseSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class WorkoutExerciseViewSet(viewsets.ModelViewSet):
    queryset = WorkoutExercise.objects.all()
    serializer_class = WorkoutExerciseSerializer

class BodyWeightLogViewSet(viewsets.ModelViewSet):
    queryset = BodyWeightLog.objects.all()
    serializer_class = BodyWeightLogSerializer