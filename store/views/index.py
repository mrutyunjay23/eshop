from django.views import View
from django.shortcuts import render, redirect
from store.models import Category, Product

class Index(View):
    def get(self, request):
        context = {}
        categories = Category.get_all_categories()
        category_id = request.GET.get('category')       
        if category_id:
            products = Product.get_products_by_category_id(category_id)
        else:
            products = Product.get_all_products()
        context['products'] = products
        context['categories'] = categories

        cart = request.session.get('cart')
        if not cart:
            cart = {}
        request.session['cart'] = cart
        return render(request, 'index.html', context)
    def post(self, request):
        product = request.POST.get('product') 
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print(cart)
        return redirect('index')