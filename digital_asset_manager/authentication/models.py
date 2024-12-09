import os
from django.db import models
from django.contrib.auth.models import User

def upload_to_directory(instance, filename):
    # Organize files into subfolders: media/assets/<username>/<filename>
    return os.path.join('assets', instance.user.username, filename)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Asset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assets")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to=upload_to_directory)  # Custom upload_to function
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
