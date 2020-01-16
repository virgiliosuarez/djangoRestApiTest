from rest_framework import serializers

from core.models.country import Country


class CountrySerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Country
        fields = '__all__'
