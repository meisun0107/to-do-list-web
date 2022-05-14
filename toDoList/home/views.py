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
    todolist = Task.objects.filter(complete=False)
    context = {'todolist': todolist}
    return render(request, template_name=template_name, context=context)


def create_task(request):
    title = request.POST.get("title")
    task = Task(title=strip_tags(title),)
    task.save()
    return redirect(reverse("home:index"))