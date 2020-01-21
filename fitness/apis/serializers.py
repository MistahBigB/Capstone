from rest_framework import serializers
from fitness import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['name']

class MuscleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MuscleGroup
        fields = ['name']

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Equipment
        fields = ['name']

class ExerciseSerializer(serializers.ModelSerializer):
    muscle_info = MuscleGroupSerializer(many=True, read_only=True, source='muscle_group')
    category_info = CategorySerializer(many=True, read_only=True, source='category')
    equipment_info = EquipmentSerializer(many=True, read_only=True, source='equipment')

    class Meta:
        model = models.Exercise
        fields = [
            'id',
            'name',
            'muscle_group',
            'muscle_info',
            'category',
            'category_info',
            'equipment',
            'equipment_info',
            'description',
            'youtube',
            'img',
        ]

class SuperSetSerializer(serializers.ModelSerializer):
    exercise_info = ExerciseSerializer(read_only=True, source='exercise')
    class Meta:
        model = models.SuperSet
        fields = [
            'exercise',
            'workout',
            'rep',
            'weight',
            'exercise_info'
        ]
class WorkoutSerializer(serializers.ModelSerializer):
    exercise_info = ExerciseSerializer(many=True, read_only=True, source='exercises')
    superset_info = SuperSetSerializer(many=True, read_only=True, source='supersets')
    class Meta:
        model = models.Workout
        fields = ['name', 'date_created', 'exercise_info', 'supersets', 'superset_info']
    # depth = 1