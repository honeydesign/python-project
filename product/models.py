from django.db import models

# Create your models here.
class PrdItem(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class FoodItem(models.Model):
    name = models.CharField(max_length=50)
    categories=models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)