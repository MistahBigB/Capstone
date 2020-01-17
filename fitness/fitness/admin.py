from django.contrib import admin

from .models import Category, MuscleGroup, Equipment, Workout, Exercise, SuperSet

admin.site.register(Category)
admin.site.register(MuscleGroup)
admin.site.register(Equipment)
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(SuperSet)