from django.db import models
import uuid
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    min_read = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    date_published = models.DateField(auto_now=True)
    last_updated = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True,blank=True, default='default.png')
    best = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    
    def __str__(self):
        return self.title



class Comment(models.Model):
    blog = models.ForeignKey(Blog, null=True, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    content = models.TextField(null=True)

    def __str__(self):
        return self.user.username