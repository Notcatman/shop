from django.shortcuts import render
from .models import Cart, Products

def crow(request):

    return render(request, "base.html")

def crow2(request):
    products = Products.objects.all()

    context = {
        "products": products
    }

    return render(request, "products.html", context)

def crow3(request, product_id):
    product = Products.objects.get(id=product_id)
    context = {
        "product": product
    }
    return render(request, "info.html", context)

def crow4(request):
    cart_item = Cart.objects.all()
    total = sum(item.product.price for item in cart_item)

    context = {
        "cart_item": cart_item,
        'total': total
    }

    return render(request, "cart.html", context)