from django.shortcuts import render
from .models import Project


def project_list(request):
    projects = Project.objects.all()
    if 'hx-request' in request.headers:
        return render(request, "projects/project_list_partial.html", {"projects": projects})
    return render(request, "projects/project_list.html", {"projects": projects})

    