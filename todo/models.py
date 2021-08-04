from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
    list_name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lists')

    def __str__(self):
        return self.list_name

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField()
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='tasks')



    