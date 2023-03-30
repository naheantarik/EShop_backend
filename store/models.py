from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='', blank=True)
    image = models.ImageField(upload_to='Media/products/')


class Category(models.Model):
    name = models.CharField(max_length=100)
