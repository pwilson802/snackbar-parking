from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Post(models.Model):
    category_choices = (
        ('story', 'story'),
        ('review', 'review'),
        ('news', 'news'),
        ('snack-bar', 'snack-bar')
    )
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=30, choices=category_choices)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    imagewide = models.ImageField(upload_to='parking_pics')
    imagesmall = models.ImageField(upload_to='parking_pics')
    byline = models.TextField()
    content = models.TextField()
    park_type = models.CharField(max_length=100, blank=True, default='')
    park_destination = models.CharField(max_length=100, blank=True, default='')
    park_difficulty = models.CharField(max_length=100, blank=True, default='')
    park_restrictions = models.CharField(max_length=100, blank=True, default='')
    head_article_byline_widescreen_margin = models.CharField(max_length=4, default='0')

    def __str__(self):
        return self.title
    
    def save_post(self):
        self.last_changed = timezone.now()
        self.save()