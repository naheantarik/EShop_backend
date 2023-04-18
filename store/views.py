from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
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

# Signup All works


def validateCustomer(customers):
    error_message = None

    if (not customers.email):
        error_message = 'Please Enter Email !!'
    elif (not customers.phone):
        error_message = 'Please Enter Phone Number !!'
    elif len(customers.phone) < 11:
        error_message = 'Phone number must 11 digit'
    elif (not customers.password):
        error_message = 'Please Enter Password !!'
    elif len(customers.password) < 6:
        error_message = 'Must be 6 digit Password'
    elif customers.isExists():
        error_message = 'Email already registered'

    return error_message


def registerUser(request):
    PostData = request.POST
    first_name = PostData.get('firstname')
    last_name = PostData.get('lastname')
    phone = PostData.get('phone')
    email = PostData.get('email')
    password = PostData.get('password')

    # Validation

    value = {'first_name': first_name, 'last_name': last_name,
             'phone': phone, 'email': email}

    error_message = None

    customers = Customer(first_name=first_name,
                         last_name=last_name,
                         phone=phone,
                         email=email,
                         password=password)

    error_message = validateCustomer(customers)

    # save

    if not error_message:
        customers.password = make_password(customers.password)
        customers.register()                                    # save all values
        return redirect('home')

    else:
        data = {
            'value': value,
            'error': error_message
        }
        return render(request, 'signup.html', data)

# end Works


def Signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return registerUser(request)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.getCustomer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                return redirect('home')
            else:
                error_message = 'Your email or password incorrect'
        else:
            error_message = 'Your email or password incorrect'

        return render(request, 'login.html', {'error': error_message})
