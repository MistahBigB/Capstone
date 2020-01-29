from django.urls import path, include
from .views import CategoryViewSet, MuscleGroupViewSet, EquipmentViewSet, ExerciseViewSet, WorkoutViewSet, SuperSetViewSet, CurrentUserView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('muscle', MuscleGroupViewSet)
router.register('equipment', EquipmentViewSet)
router.register('exercise', ExerciseViewSet)
router.register('workout', WorkoutViewSet)
router.register('superset', SuperSetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('current_user/', CurrentUserView.as_view()),
    path('api-auth', include('rest_framework.urls'))
]
