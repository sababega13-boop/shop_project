from django.shortcuts import render

def home_view(request):
    return render(request, 'shop_app/home.html')

def products_view(request):

    products = [
        {"name": "Laptop", "price": 2500},
        {"name": "Mouse", "price": 80},
        {"name": "Keyboard", "price": 150},
        {"name": "Monitor", "price": 700},
    ]
    return render(request, 'shop_app/products.html', {'products': products})
