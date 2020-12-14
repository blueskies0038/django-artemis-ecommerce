from django.db import models
from django.contrib.auth.models import User
from aesthetic import models as collection_model

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    def get_email(self):
        return self.email

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    description = models.TextField(null=True)
    featured = models.ImageField(null=True, blank=True)
    collection = models.ForeignKey(collection_model.Collection, blank=True, null=True, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.featured.url
        except:
            url = ''
        return url

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField()

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        print('URL', url)
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.items.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_tax(self):
        orderitems = self.items.all()
        tax = sum([item.get_total for item in orderitems]) * 0.0875
        return tax

    @property
    def get_shipping(self):
        orderitems = self.items.all()
        total = sum([item.get_total for item in orderitems])
        if total > 75:
            return 0
        return 7

    @property
    def get_cart_items(self):
        orderitems = self.items.all()
        total = sum([item.quantity for item in orderitems if item.product.active])
        return total

    @property
    def get_final_amount(self):
        total = self.get_cart_total + self.get_shipping + self.get_tax
        return total

    @property
    def get_order_items(self):
        all_items = self.items.all()
        return all_items

    def get_all_items(self):
        all_items = self.items.all()
        return all_items


class OrderItem(models.Model):
    product = models.ForeignKey(Product, related_name="items" ,on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, related_name="items" , on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.product.name

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, related_name="address", on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, related_name="address", on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        full_address = f"{self.address} {self.city}, {self.state}, {self.zipcode}"
        return full_address

class HomeSlide(models.Model):
    name = models.CharField(max_length=100, blank=True)
    caption = models.TextField(blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        print('URL', url)
        return url

