from django.shortcuts import render

from modalFBV.models import Projects
from .forms import ProjectsForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST


def modalfbv_index(request):
    return render(request, 'modal-fbv-index.html')


def project_list(request):
    return render(request, 'partials/project_list.html', {'projects': Projects.objects.all(), })


def add_project(request):
    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'projectListChanged'})
    else:
        form = ProjectsForm()
    return render(request, 'partials/project_form.html', {
            'form': form,
        })


def edit_project(request, pk):
    project = get_object_or_404(Projects, pk=pk)
    if request.method == 'POST':
        form = ProjectsForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'projectListChanged'})
    else:
        form = ProjectsForm(instance=project)
    return render(request, 'partials/project_form.html', {
            'form': form,
            'project': project,
        })


@require_POST
def remove_project(request, pk):
    project = get_object_or_404(Projects, pk=pk)
    project.delete()
    return HttpResponse(status=204, headers={'HX-Trigger': 'projectListChanged'})
