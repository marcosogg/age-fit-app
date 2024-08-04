from rest_framework import serializers
from .models import CustomUser, Exercise, Program, WorkoutDay, ProgramExercise, Workout, WorkoutExercise, BodyWeightLog

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'date_of_birth', 'height', 'fitness_level')
        extra_kwargs = {'password': {'write_only': True}}

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class WorkoutDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutDay
        fields = '__all__'

class ProgramExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramExercise
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

class WorkoutExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExercise
        fields = '__all__'

class BodyWeightLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyWeightLog
        fields = '__all__'
