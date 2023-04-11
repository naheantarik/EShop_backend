from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

# Register your models here.


admin.site.register(Product, AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)
