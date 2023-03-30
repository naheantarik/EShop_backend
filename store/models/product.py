from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, default='', blank=True)
    image = models.ImageField(upload_to='Media/products/')

    def __str__(self):
        return self.name
