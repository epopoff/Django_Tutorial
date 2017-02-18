import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Ticket(models.Model):
    user = models.ForeignKey('auth.User')
    problem = models.CharField(max_length=200)
    offer = models.TextField()
    effect = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now())
    profit = models.BooleanField(default=False)

    def __str__(self):
        return self.problem
