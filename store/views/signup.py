from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models import Customer

def validate_user(customer):
        # validation
        error_message = None
        if not customer.first_name:
            error_message = "First name required !"
        elif len(customer.first_name) < 2:
            error_message = "First name must be include 2 or more characters"
        elif not customer.last_name:
            error_message = "Last name required !"
        elif len(customer.last_name) < 2:
            error_message = "Last name must be include 2 or more characters"
        elif not customer.phone_number:
            error_message = "Last name required !"
        elif len(customer.phone_number) != 10:
            error_message = "Phone number must include 10 numbers"
        elif not customer.phone_number:
            error_message = "Password required !"
        elif len(customer.phone_number) < 4:
            error_message = "First name must be include 4 or more characters"
        elif customer.is_exist():
            error_message = "Email address already registered !"   
        return error_message 


def register_user(request):
    context = {}
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    phone_number = request.POST.get("phone_number")
    email = request.POST.get("email")
    password = request.POST.get("password")

    values = {
        'first_name': first_name,
        'last_name' : last_name,
        'phone_number': phone_number,
        'email' : email
    }

    customer = Customer(first_name = first_name,
                            last_name= last_name,
                            phone_number=phone_number,
                            email= email,
                            password= password)

    error_message = validate_user(customer)

    if error_message:
        context['error_message'] = error_message
        context['values'] = values
        return render(request, 'signup.html', context)
    else:
        customer.password = make_password(customer.password)
        customer.register()
        return redirect("index")


def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')

    else:
        return register_user(request)