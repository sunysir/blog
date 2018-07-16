from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

# Create your models here.
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name',]

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name',]

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateField(default=datetime.utcnow)
    modified_time = models.DateField(default=datetime.utcnow)
    execrpt = models.CharField(max_length=300, blank=True)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category)
    author = models.ForeignKey(User)
    view = models.PositiveIntegerField(default=0)
    def increase_views(self):
        self.view += 1
        self.save(update_fields=['view'])
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    class Meta:
        ordering = ['-created_time']
