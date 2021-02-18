from django.db import models
from django.contrib.auth.models import User
from app.good.models import Good


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goods = models.ManyToManyField(Good)
    date = models.DateTimeField(auto_now_add=True)
