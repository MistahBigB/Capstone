from rest_framework import serializers
from fitness import models

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = {
            'id',
            'name',
            'muscle_group',
            'category',
            'equipment',
            'description',
            'youtube',
            'img',
            'weight',
            'reps'
        }
        model = models.Exercise