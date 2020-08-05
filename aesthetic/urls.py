from django.urls import path
from . import views

urlpatterns = [
    path('collections/', views.collections, name='collections'),
    path('<int:collection_id>/', views.detail, name='detail'),
]