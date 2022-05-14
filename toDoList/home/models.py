from django.db import models
from django.utils import timezone
from django.conf import settings


class Task(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(blank=True, null=True)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=None, null=False, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
