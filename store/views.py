from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models.product import Product  # this model is model folter
from .models.category import Category  # this model is model folter
from .models.customer import Customer  # this model is model folter
from .validuser import registerUser

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

    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return registerUser(request)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
