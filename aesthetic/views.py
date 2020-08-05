from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
import datetime
from .models import *
from store.utils import cookieCart, cartData, guestOrder

# Create your views here.

def collections(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'cartItems': cartItems}
    return render(request, 'aesthetic/collections.html', context)

def detail(request, collection_id):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    collection = get_object_or_404(Collection, pk=collection_id)
    context = {'collection': collection, 'cartItems': cartItems}
    return render(request, 'aesthetic/detail.html', context)