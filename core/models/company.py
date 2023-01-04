from django.db import models
from core.models.country import Country


class Company(models.Model):
    name = models.CharField("Company Name", max_length=100)
    address = models.TextField("Address", blank=True, null=True)
    postalCode = models.CharField("Postal Code", max_length=100)
    logo = models.CharField("Logo", max_length=100)
    country = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + self.address


