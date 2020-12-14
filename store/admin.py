from django.contrib import admin
from django.utils.html import mark_safe
from .models import *


class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)

    list_display = ("name", "get_thumbnail",)

    search_fields = ("name",)

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.featured.url}" />')

    get_thumbnail.short_description = "Thumbnail"


@admin.register(ShippingAddress)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ("customer", "full_address",)

    def full_address(self, obj):
        address = [obj.address, obj.city, obj.state, obj.zipcode]
        return " ".join(address)
    full_address.short_description = "Shipping Address"

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("__str__", "customer", "get_customer_email", "order_items", "get_address",)

    def order_items(self, obj):
        all_items = list(obj.get_all_items())
        all_order_items = []
        for item in all_items:
            all_order_items.append(str(item))
        return ", ".join(all_order_items)
    order_items.short_description = "Order Items"

    def get_address(self, obj):
        address = obj.address.get()
        return address
    get_address.short_description = "Shipping Address"

    def get_customer_email(self, obj):
        return obj.customer.email
    get_customer_email.short_description = "Email"

@admin.register(HomeSlide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ("__str__", "get_thumbnail",)
    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.image.url}" />')
    get_thumbnail.short_description = "Thumbnail"


admin.site.register(Customer)
admin.site.register(Image)
admin.site.register(OrderItem)