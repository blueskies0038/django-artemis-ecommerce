from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, guestOrder


def store(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    slides = HomeSlide.objects.all()
    context = {'cartItems': cartItems, 'slides': slides, }
    messages.success(request, "Welcome to ARTEMIS")
    return render(request, 'store/store.html', context)


def all(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    page = request.GET.get("page", 1)
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 12, orphans=3)
    try:
        products = paginator.page(int(page))
        context = {'products': products, 'cartItems': cartItems}
        return render(request, 'store/all.html', context)
    except EmptyPage:
        products = paginator.page(1)
        context = {'products': products, 'cartItems': cartItems}
        return redirect('store/all.html', context)


def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    """for item in items:
        product_id = int(item["product"]["id"])
        product = Product.objects.get(id=product_id)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        if not product.active:
            orderItem.delete()"""

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems, }
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add' and product.active:
        orderItem.quantity = 1
        orderItem.save()
    elif action == 'remove':
        orderItem.delete()

    return JsonResponse('Item was updated', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == float(order.get_final_amount):
        for o in order.get_order_items:
            ord_id = o.id
            item = OrderItem.objects.get(id=ord_id)
            print(str(o), str(item.product))
            if item.product.amount == 1:
                item.product.active = False
            else:
                item.product.amount -= 1
        order.complete = True
    order.save()

    ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
    )

    return JsonResponse('Payment submitted..', safe=False)


def about(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'cartItems': cartItems}
    return render(request, 'store/about.html', context)


def detail(request, product_id):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    try:
        product = get_object_or_404(Product, pk=product_id)
        context = {'product': product, 'cartItems': cartItems}
        return render(request, 'store/detail.html', context)
    except:
        return render(reverse("all"))


def slider(request):
    product = Product.object.first()
    context = {'product': product}
    return render(request, 'store/detail.html', context)



