from django.shortcuts import render, redirect
from .models import Product, Order


def catalog(request):
    all_products = Product.objects.all()
    return render(request, 'shop/catalog.html', {'products': all_products})


def orders(request):
    if not request.user.is_authenticated:
        return redirect('signin')

    orders_ = Order.objects.filter(user=request.user)
    return render(request, 'shop/orders.html', {'orders': orders_})


def order_create(request, product_id):
    if not request.user.is_authenticated:
        return redirect('signin')

    if request.method == 'POST':
        Order.objects.create(
            user=request.user,
            product_id=product_id,
            delivery_address=request.POST.get('delivery_address')
        )
        return redirect('orders')
    return render(request, 'shop/order_create.html', {
        'product': Product.objects.get(id=product_id)
    })


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/product_detail.html', {
        'product': product
    })
