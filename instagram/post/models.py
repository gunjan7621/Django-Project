from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, default="Untitled")
    user = models.CharField(max_length=100, default="Anonymous")
    content = HTMLField(max_length=100)
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    saved_by_user = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)


