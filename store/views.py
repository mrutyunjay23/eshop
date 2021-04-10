from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category, Customer
# Create your views here.


def index(request):
    context = {}
    products = Product.get_all_products()
    categories = Category.get_all_categories()
    context['products'] = products
    context['categories'] = categories
    return render(request, 'index.html', context)

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')

    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        password = request.POST.get("password")

        customer = Customer(first_name = first_name,
                            last_name= last_name,
                            phone_number=phone_number,
                            email= email,
                            password= password)

        customer.register()
        return HttpResponse("Signup Success ")

