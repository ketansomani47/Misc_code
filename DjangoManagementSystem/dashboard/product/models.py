from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.FloatField()

    class Meta:
        db_table = 'product'


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=250)
    address = models.FloatField()

    class Meta:
        db_table = 'user'


class Cart(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_list')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    class Meta:
        db_table = 'cart'
