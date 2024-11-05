from django.db import models


class Task(models.Model):
    user_profile = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= 'Task'
        verbose_name_plural= 'Tasks'
