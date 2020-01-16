from django.contrib import admin

from core.models.company import Company
from core.models.country import Country

admin.site.register(Country)
admin.site.register(Company)
