from rest_framework import viewsets
from fitness import models
from .serializers import CategorySerializer, MuscleGroupSerializer, EquipmentSerializer, ExerciseSerializer, WorkoutSerializer, SuperSetSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer

class MuscleGroupViewSet(viewsets.ModelViewSet):
    queryset = models.MuscleGroup.objects.all()
    serializer_class = MuscleGroupSerializer

    def get_queryset(self):
        name = self.request.GET.get("muscle_group", None)

        if name:
            return models.MuscleGroup.objects.filter(name__iexact=muscle_group)

        return models.MuscleGroup.objects.all()

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = models.Equipment.objects.all()
    serializer_class = EquipmentSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = models.Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        name = self.request.GET.get("name", None)

        if name:
            return models.Exercise.objects.filter(name__iexact=name)

        return models.Exercise.objects.all()

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = models.Workout.objects.all()
    serializer_class = WorkoutSerializer
    
class SuperSetViewSet(viewsets.ModelViewSet):
    queryset = models.SuperSet.objects.all()
    serializer_class = SuperSetSerializer

