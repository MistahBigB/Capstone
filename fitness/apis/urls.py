from django.urls import path
from .views import ExerciseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ExerciseViewSet, basename='exercise')
urlpatterns = router.urls