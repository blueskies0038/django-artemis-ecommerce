from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
import datetime
from .models import *
from store.utils import cookieCart, cartData, guestOrder
from store import models as store_models

# Create your views here.

def collections(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    collection_previews = CollectionPreview.objects.all()
    context = {'cartItems': cartItems, 'collection_previews': collection_previews}
    return render(request, 'aesthetic/collections.html', context)

def detail(request, collection_id):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    collection = get_object_or_404(Collection, pk=collection_id)
    products = store_models.Product.objects.all().filter(collection=collection)
    collection_images = CollectionImage.objects.all().filter(collection=collection)
    images = []
    i = 0
    if len(products) > len(collection_images):
        while i < len(collection_images):
            images.append(products[i])
            images.append(collection_images[i])
            i += 1
        images.append(products[i])
    elif len(products) == len(collection_images):
        while i < len(collection_images):
            images.append(products[i])
            images.append(collection_images[i])
            i += 1
    else:
        while i < len(products):
            images.append(collection_images[i])
            images.append(products[i])
            i += 1
        images.append(collection_images[i])

    context = {'collection': collection,'images': images, 'cartItems': cartItems}
    return render(request, 'aesthetic/detail.html', context)