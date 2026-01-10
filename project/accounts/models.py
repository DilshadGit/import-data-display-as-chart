from django.db import models
from django.contrib.auth.models import User





class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, default='')
    email = models.EmailField(max_length=254, default='')
    city = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)
    weblink = models.URLField(max_length=200, default='')

    def __str__(self):
        return self.user.username
