from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
        
class MuscleGroup(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Workout(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=50)
    muscle_group = models.ManyToManyField(MuscleGroup, related_name='exercises')
    category = models.ManyToManyField(Category, related_name='exercises')
    equipment = models.ManyToManyField(Equipment, related_name='exercises')
    description = models.TextField()
    youtube = models.URLField()
    img = models.ImageField(upload_to='exercise_images/')
    workouts = models.ManyToManyField(Workout, related_name='exercises', through='SuperSet')

    def __str__(self):
        return self.name

class SuperSet(models.Model):
    workout = models.ForeignKey(Workout, related_name='supersets', on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, related_name='supersets', on_delete=models.CASCADE)
    rep = models.IntegerField()
    weight = models.IntegerField()
    

