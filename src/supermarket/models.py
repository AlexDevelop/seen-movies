from django.db import models

from movies.models import BaseModel


class Supermarket(BaseModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ProductType(BaseModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=30)
    price = models.FloatField(blank=True, null=True, default=0)
    product_type = models.ForeignKey("ProductType")

    def __str__(self):
        return "[{}] {} {}".format(self.product_type,  self.name, self.price)


class GroceryList(BaseModel):
    amount = models.IntegerField()
    product = models.ForeignKey("Product")
    supermarket = models.ForeignKey("Supermarket")
