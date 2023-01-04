from django.db import models


class Country(models.Model):
    name = models.CharField("Country Name", max_length=100)
    iso_code = models.CharField("ISO Code", max_length=3)

    def __str__(self):
        return self.name
        

