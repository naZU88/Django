from django.utils import timezone
from django.db import models

# Create your models here.

#id добавится автоматически
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    adress = models.CharField(max_length=200)
    date_registr = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, phone_number: {self.phone_number}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)    
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quant = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='products/', null=True, blank=True)
    date_add = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Priduct_name: {self.name}, price: {self.price}'    


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)    
    date_ordered = models.DateTimeField(default=timezone.now)
