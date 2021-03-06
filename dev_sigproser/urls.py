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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # path to backend end points
    path('admin/', admin.site.urls, name='backend'),

    # path to djoser end points
    path('auth/', include('djoser.urls'), name='djoser'),
    path('auth/', include('djoser.urls.jwt'), name='djoser_jwt'),

    # path to core end points
    path('core/', include('core.urls'), name='plugin_core'),
]
