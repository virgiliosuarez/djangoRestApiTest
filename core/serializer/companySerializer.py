from rest_framework import serializers

from core.models.company import Company


class CompanySerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Company
        fields = '__all__'
