from django.shortcuts import render

# Create your views here.

def collections(request):
    context = {}
    return render(request, 'aesthetic/collections.html', context)