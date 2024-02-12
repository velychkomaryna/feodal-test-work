from django.urls import path
from .views import TaskViewsSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"task", TaskViewsSet, basename="task-api")
urlpatterns = router.urls
