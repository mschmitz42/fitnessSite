from django.db import models
from django.contrib.auth.models import User


class Measurement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=128)
    date = models.DateField()
    value = models.FloatField()


class Macro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    calories = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()
    fiber = models.FloatField()
    protein = models.FloatField()


