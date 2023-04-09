from django.shortcuts import render
from .models.product import Product, Category

# Create your views here.


def index(request):
    prduct = Product.get_all_product()
    category = Category.get_all_category()

    return render(request, 'index.html', {'products': prduct}, {'categorys': category})
