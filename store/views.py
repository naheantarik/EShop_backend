from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product  # this model is model folter
from .models.category import Category  # this model is model folter
from .models.customer import Customer  # this model is model folter

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
        PostData = request.POST
        first_name = PostData.get('firstname')
        last_name = PostData.get('lastname')
        phone = PostData.get('phone')
        email = PostData.get('email')
        password = PostData.get('password')

        error_message = None

        # Validation

        if (not email):
            error_message = 'Please Enter Email !!'
        elif (not phone):
            error_message = 'Please Enter Phone Number !!'
        elif len(phone) < 11:
            error_message = 'Phone number must 11 digit'
        elif (not password):
            error_message = 'Please Enter Password !!'
        elif len(password) < 6:
            error_message = 'Must be 6 digit Password'

        # save

        if not error_message:
            print(first_name, last_name, phone, email, password)

            customers = Customer(first_name=first_name,
                                 last_name=last_name,
                                 phone=phone,
                                 email=email,
                                 password=password)
            customers.register()

        else:
            return render(request, 'signup.html', {'error': error_message})
