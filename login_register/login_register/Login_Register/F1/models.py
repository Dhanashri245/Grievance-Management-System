from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('employee', 'Employee'),
        ('user', 'User'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
class Complaint(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    complaint_text = models.TextField()
    photo = models.ImageField(upload_to='complaint_photos/', blank=True, null=True)

    def __str__(self):
        return f"Complaint from {self.name}"