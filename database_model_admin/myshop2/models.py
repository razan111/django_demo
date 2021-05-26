from django.db import models

# Create your models here.

class Customer(models.Model):
    #attr
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=15, null=False)
    email = models.EmailField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "Name: "+self.first_name+" "+self.last_name+"    Email: "+self.email


class Products(models.Model):
    catagory = models.CharField(max_length=100, null=False)
    product_name = models.CharField(max_length=100)
    Product_descriptions = models.TextField()
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.product_name
