"""dev_sigproser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from core.views.countryViews import CountryViews
from django.urls import path

urlpatterns = [
    path('country/', CountryViews.country_list_create, name='country_list_create'),
    path('country_paginate/', CountryViews.country_list_paginate, name='country_list_paginate'),
    path('country/<int:pk>/', CountryViews.country_detail, name='country_detail'),
]
