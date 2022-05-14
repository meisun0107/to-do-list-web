from django.shortcuts import render
from .models import Task
from django.utils.html import strip_tags
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib.auth.decorators import login_required
"""
function: index

set path for homepage
"""

def index(request):
    template_name = "home/templates/index.html"
    if request.user.is_authenticated:
        todolist = Task.objects.filter(user=request.user)
    else:
        todolist = {}
    context = {'todolist': todolist}
    return render(request, template_name=template_name, context=context)

@login_required
def sorting(request):
    template_name = "home/templates/index.html"
    if request.method == "POST":
        if request.POST.get("sortby") == "added-date" :
            todolist = Task.objects.filter(user=request.user).order_by('create_date')
        elif request.POST.get("sortby") == "due-date":
            todolist = Task.objects.filter(user=request.user).order_by('due_date')
        else:
            todolist = Task.objects.filter(user=request.user)

    context = {'todolist': todolist}
    print(todolist)
    return render(request, template_name=template_name, context=context)

@login_required
def create_task(request):
    title = request.POST.get("title")
    due_date = request.POST.get("due_date")
    if request.user.is_authenticated:
        task = Task(title=strip_tags(title), due_date = due_date, user=request.user)
    else:
        task = Task(title=strip_tags(title), due_date = due_date, )
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
    title = request.POST.get("title")
    due_date = request.POST.get("due_date")
    task.due_date = due_date
    task.save()

    return redirect(reverse("home:index"))