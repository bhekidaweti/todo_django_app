from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=30, blank=False)
    description = models.CharField(max_length= 100, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.task}, {self.description}"
    
