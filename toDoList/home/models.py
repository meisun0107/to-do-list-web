from django.db import models
from django.utils import timezone
 
class Task(models.Model):
    title=models.CharField(max_length=100)
    details=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    due_date=models.DateTimeField(blank=True, null=True)
    complete = models.BooleanField(default=False)

 
    def __str__(self):
        return self.title
