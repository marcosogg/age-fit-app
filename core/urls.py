from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    home,  # Add this import
    CustomUserViewSet,
    ExerciseViewSet,
    ProgramViewSet,
    WorkoutDayViewSet,
    ProgramExerciseViewSet,
    WorkoutViewSet,
    WorkoutExerciseViewSet,
    BodyWeightLogViewSet
)

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'exercises', ExerciseViewSet)
router.register(r'programs', ProgramViewSet)
router.register(r'workout-days', WorkoutDayViewSet)
router.register(r'program-exercises', ProgramExerciseViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'workout-exercises', WorkoutExerciseViewSet)
router.register(r'body-weight-logs', BodyWeightLogViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),
]