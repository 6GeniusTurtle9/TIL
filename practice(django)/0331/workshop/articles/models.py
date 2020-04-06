from django.db import models

# Create your models here.
class Article(models.Model):
    title = model.CharField(max_length=20)
    content = model.TextField()
    created_at = model.DateTimeField(auto_now_add=True)
    updated_at = model.DateTimeField(auto_now=True)