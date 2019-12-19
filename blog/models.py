from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=30)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='parking_pics')
    byline = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title
    
    def save_post(self):
        self.last_changed = timezone.now()
        self.save()