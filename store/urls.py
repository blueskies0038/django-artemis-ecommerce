from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('all', views.all, name='all'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('about/', views.about, name='about'),
    path('<int:product_id>/', views.detail, name='detail'),

]