from django.shortcuts import render
from .models.product import Product, Category

# Create your views here.


def home(request):
    products = None
    category = Category.get_all_category()

    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_product_by_categoryId(categoryID)
    else:
        products = Product.get_all_product()

    data = {}
    data['products'] = products
    data['categorys'] = category

    return render(request, 'index.html', data)


def Signup(request):
    return render(request, 'signup.html')
