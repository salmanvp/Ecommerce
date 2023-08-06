from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    data_added=models.DateField(auto_now=True)

    def subtotal(self):
        return self.quantity*self.product.price

    def __str__(self):
        return self.product.name


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    address=models.TextField()
    phone=models.CharField(max_length=10)
    order_status=models.CharField(max_length=30,default="Pending")
    delivery_status=models.CharField(max_length=30,default="pending")
    no_of_items=models.IntegerField()
    data_added=models.DateTimeField(auto_now_add=True)

    def subtotal(self):
        return self.no_of_items*self.product.price
    def __str__(self):
      return self.user.username



class Account(models.Model):
    acctnumber=models.CharField(max_length=20)
    actype=models.CharField(max_length=20)
    amount=models.IntegerField()
    def __str__(self):
        return self.acctnumber