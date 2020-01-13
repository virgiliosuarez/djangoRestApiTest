from django.db import models

from core.models.country import Country
from core.serializer.countrySerializer import CountrySerializer


class CountryManager(models.Manager):
    request = ''

    def __init__(self, request):
        self.request = request

    """
      Get one country by pk
    """

    def get(self, pk):
        country = self.find_by_pk(pk)
        if not country:
            return False
        serializer = CountrySerializer(country, context={'request': self.request}, many=False)
        return serializer.data

    """
    Get all country
    """

    def get_all(self):
        country = Country.objects.all()
        serializer = CountrySerializer(country, context={'request': self.request}, many=True)
        return serializer.data

    """
    Create a new Country
    """

    def create(self):
        serializer = CountrySerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()

        return serializer

    """
    Update Country info
    """
    def update(self, pk):
        country = self.find_by_pk(pk)
        serializer = CountrySerializer(country, data=self.request.data, context={'request': self.request})
        if serializer.is_valid():
            serializer.save()

        return serializer

    """
    Delete a country
    """

    def delete(self, pk):
        country = self.find_by_pk(pk)
        country.delete()
        return True

    """
    Find country by primary key
    """

    @staticmethod
    def find_by_pk(pk):
        try:
            country = Country.objects.get(pk=pk)
            return country
        except Country.DoesNotExist:
            return False
