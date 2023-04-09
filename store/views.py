from django.shortcuts import render
from .models.product import Product, Category

# Create your views here.


def index(request):
    products = None
    category = Category.get_all_category()

    categoryId = request.GET.get('categories')
    if categoryId:
        products = Product.get_all_product_by_categoryId(categoryId)
    else:
        products = Product.get_all_product()

    data = {}
    data['products'] = products
    data['categorys'] = category

    return render(request, 'index.html', data)
