from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Teacher(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='teacher')
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Feedback(models.Model):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name='feedbacks')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
