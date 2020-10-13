from django.db import models
from django.contrib.auth.models import User

import uuid

users_type_choices = (
    ('seller', 'seller'),
    ('customer', 'customer')
)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=100, choices = users_type_choices)

class Seller(models.Model):
    user_id = models.IntegerField() # from models User.id
    store_id = models.IntegerField() # from models Store.id

class Customer(models.Model):
    user_id = models.IntegerField() # from models User.id
    address = models.TextField()
    pict = models.ImageField(upload_to="pict/%Y/%m/", null=True)

class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    pict = models.ImageField(upload_to="pict/%Y/%m/", null=True)