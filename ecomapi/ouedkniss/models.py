from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client (models.Model):
    phone_number=models.CharField(max_length=20)
    user= models.OneToOneField(User ,on_delete=models.CASCADE ,null=True, blank=True)

class Seller (models.Model):
    phone_number=models.CharField(max_length=200)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    state=models.CharField(max_length=150)


class Product (models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    price=models.IntegerField(default=0)
    owner=models.ForeignKey(Seller ,on_delete=models.CASCADE)

class Order (models.Model):
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    status=models.CharField(default="in cart",max_length=150)

class Paiement(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(default="online", max_length=20)
    status = models.CharField( default="pending" ,max_length=20,)
    transaction_date = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(default="DA", max_length=3)
    confirmation_number = models.CharField(max_length=50, unique=True , blank= True ,null= True)

    
    
