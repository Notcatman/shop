from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Products(models.Model):
    name = models.CharField(max_length=300, null=False)
    description = models.TextField(blank=True, default="Hi!")
    price = models.FloatField(null=False, validators=[MaxValueValidator(9999), MinValueValidator(0)])

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.price}$'
    
class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name}'
    