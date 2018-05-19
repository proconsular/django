from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    liked_users = models.ManyToManyField(User, related_name="liked_books")
    uploader = models.ForeignKey(User, related_name="uploaded_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
