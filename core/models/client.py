from django.db import models
from core.models.country import Country


class Client(models.Model):
    firstName = models.CharField("First Name", max_length=100)
    lastName = models.CharField("Last Name", max_length=255)
    email = models.EmailField("Email")
    phoneNumber = models.CharField("Phone Number", max_length=100)
    city = models.CharField("City", max_length=100)
    address = models.TextField("Address", max_length=100)
    naturalPerson = models.BooleanField("Natural Person")
    businessName = models.CharField("Business Name", max_length=100, blank=True, null=True)
    country = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + self.email


