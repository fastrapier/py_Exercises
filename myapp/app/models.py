from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_of_product = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField
    creation_date = models.DateTimeField


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # product
    comment = models.TextField
    creation_date = models.DateTimeField


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.IntegerField


class aa(models.Model):
    title = models.CharField(max_length=10)
