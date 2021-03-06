from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models import Customer

class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        context = {}
        email = request.POST.get('email')
        password = request.POST.get('password')

        customer = Customer.get_customer_by_email(email)
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                return redirect('index')
            else:
                error_message = "Invalid Password"
        else:
            error_message = "Invalid Email"

        context['error_message'] = error_message
        return render(request, 'login.html', context)

def logout(request):
    request.session.clear()
    return redirect('login')