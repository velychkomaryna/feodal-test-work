from .models import Task
from django.shortcuts import get_object_or_404
from .serializers import TaskSerializer
from .permissions import IsOwner
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from rest_framework import status


class TaskViewsSet(viewsets.ModelViewSet):

    permission_classes = [IsOwner]
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category"]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
