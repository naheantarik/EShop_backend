from django.shortcuts import render, redirect
from .models.customer import Customer

# SignUp validations Page


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
        customers.register()                                    # save all values
        return redirect('home')

    else:
        data = {
            'value': value,
            'error': error_message
        }
        return render(request, 'signup.html', data)
