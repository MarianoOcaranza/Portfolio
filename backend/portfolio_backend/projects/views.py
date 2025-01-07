from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Project
from .serializers import ProjectSerializer

# Create your views here.
class ProjectView(ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer