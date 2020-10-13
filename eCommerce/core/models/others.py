from django.db import models

class Shiper(models.Model):
    name = models.CharField(max_length=100)
    ship_fee = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)