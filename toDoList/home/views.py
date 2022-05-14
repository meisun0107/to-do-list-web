from django.shortcuts import render
from .models import Task
"""
function: index

set path for homepage
"""

def index(request):
    template_name = "home/templates/index.html"
    todolist = Task.objects.filter(complete=False)
    context = {'todolist': todolist}
    print(todolist)
  
    return render(request, template_name=template_name, context=context)
