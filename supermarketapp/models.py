from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    category_name=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.category_name

class ProductsDb(models.Model):
    product_name=models.CharField(max_length=100)


    def __str__(self):
        return self.product_name
