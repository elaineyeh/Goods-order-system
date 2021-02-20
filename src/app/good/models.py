from django.db import models


# Create your models here.
class Good(models.Model):
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
