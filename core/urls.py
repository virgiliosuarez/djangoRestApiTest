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
from django.urls import path

from core.views.companyView import CompanyListCreateView, CompanyDetailDestroyUpdateView
from core.views.countryView import CountryListCreateView, CountryDetailDestroyUpdateView
from core.views.userProfileView import UserProfileListCreateView, UserProfileDetailView

urlpatterns = [
    # path to profiles end points
    path("all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
    path("profile/<int:pk>", UserProfileDetailView.as_view(), name="profile"),

    # path to country end points
    path('country', CountryListCreateView.as_view(), name='country_list_create'),
    path('country/<int:pk>', CountryDetailDestroyUpdateView.as_view(), name='country_detail_destroy_update'),

    # path to company end points
    path('company', CompanyListCreateView.as_view(), name='company_list_create'),
    path('company/<int:pk>', CompanyDetailDestroyUpdateView.as_view(), name='company_detail_destroy_update'),
]
