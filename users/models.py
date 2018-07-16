from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    nickname = models.CharField(max_length=30)
    user = models.OneToOneField(User)
