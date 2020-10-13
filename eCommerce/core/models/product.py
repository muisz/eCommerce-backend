from django.db import models

from .user import Profile

class Item(models.Model):
    store_id = models.IntegerField()
    name = models.CharField(max_length=100)
    stock = models.IntegerField()
    price = models.FloatField()
    desc = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    date_edited = models.DateField(null=True)

class Category(models.Model):
    item_id = models.IntegerField()
    category = models.CharField(max_length=100)

class ItemSpecification(models.Model):
    item_id = models.IntegerField()
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

class ItemPicture(models.Model):
    item_id = models.IntegerField()
    pict = models.ImageField(upload_to="photo/%Y/%m/")

class ItemReview(models.Model):
    item_id = models.IntegerField()
    review_id = models.IntegerField(null=True) # for reply review
    user_id = models.IntegerField()
    review = models.TextField()
    rating = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

class ItemReviewPictures(models.Model):
    review_id = models.IntegerField()
    pict = models.ImageField(upload_to="photo/%Y/%m/")

class ItemFavorit(models.Model):
    item_id = models.IntegerField()
    user_id = models.IntegerField()
    date = models.DateField(auto_now_add=True)

# order
class Order(models.Model):
    user_id = models.IntegerField()
    item_id = models.IntegerField()
    amount = models.IntegerField()
    is_cancel = models.BooleanField(default=False)
    is_pay = models.BooleanField(default=False)
    is_confirm = models.BooleanField(default=False) # is_confirm true when user confirm that item is arrive to the customer
    date_created = models.DateField(auto_now_add=True)
    date_pay = models.DateField(null=True)

class ItemReturn(models.Model):
    order_id = models.IntegerField()
    reason = models.TextField()
    date = models.DateField(auto_now_add=True)