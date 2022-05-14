from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("sorting/", views.sorting, name="sorting"),
    path("create_task/", views.create_task, name="create-task"),
    path("change_status/", views.change_status, name="change-status"),
    path("delete_task/", views.delete_task, name="delete-task"),
    path("edit_task/", views.edit_task, name="edit-task"),
  ]
