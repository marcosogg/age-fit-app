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
    
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import CustomUserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return Response({'detail': 'Login successful'}, status=status.HTTP_200_OK)
    return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def logout_user(request):
    logout(request)
    return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)