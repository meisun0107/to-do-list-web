from django.shortcuts import render
from .models import Task
from django.utils.html import strip_tags
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
"""
function: index

set path for homepage
"""

def index(request):
    template_name = "home/templates/index.html"
    if request.user.is_authenticated:
        todolist = Task.objects.filter(user=request.user)
    else:
        todolist = Task.objects.filter(user=None)
    context = {'todolist': todolist}
    return render(request, template_name=template_name, context=context)


def create_task(request):
    title = request.POST.get("title")
    if request.user.is_authenticated:
        task = Task(title=strip_tags(title),user=request.user)
    else:
        task = Task(title=strip_tags(title),user=None)
    task.save()
    return redirect(reverse("home:index"))

def change_status(request):
    task = Task.objects.get(id=request.POST.get("id"))
    status = request.POST.get("status")
    task.complete = status
    task.save()

    return redirect(reverse("home:index"))

def delete_task(request):
    task = Task.objects.get(id=request.POST.get("id"))
    task.delete()

    return redirect(reverse("home:index"))

def edit_task(request):
    task = Task.objects.get(id=request.POST.get("id"))
    task.delete()

    return redirect(reverse("home:index"))