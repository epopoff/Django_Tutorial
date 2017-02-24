import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Ticket(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
