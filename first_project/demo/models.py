from django.db import models

# Create your models here.

class Address(models.Model):
    Name = models.CharField(max_length=100)
    Home_number = models.CharField(max_length=20)
    City = models.CharField(max_length=100)
    Dist = models.CharField(max_length=100)
    Division = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)

    def __str__(self):
        return self.Name+ " "+self.City+ "  "+self.Country

class Razan(models.Model):
    Quantaty = models.DecimalField()
    Price = models.FloatField(default=0.0)
    Qulity = models.CharField(max_length=20)

    def __str__(self):
        return self.Qulity+" "+self.Price


