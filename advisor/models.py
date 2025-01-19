
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    instagram_id = models.CharField(max_length=30, blank=True)

class UserActivity(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)  # 'fitness' or 'gift'
    answers = models.JSONField()
    recommendation = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

class Activity(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    target_area = models.CharField(max_length=100)
    health_benefit = models.TextField()

    def __str__(self):
        return self.name