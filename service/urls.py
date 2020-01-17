"""service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from requests import request

from sneakers_colors_sizes_rel.api import SneakersColorsSizesRelSearch

urlpatterns = [
    path('', include("sizes.urls")),
    path('', include('colors.urls')),
    path('', include('sneakers.urls')),
    path('', include('sneakers_colors_sizes_rel.urls')),
    url(r'^api/v0/search/', SneakersColorsSizesRelSearch, name='search'),
    url(r'^api/v0/search/(?P<name>[a-zA-Z])*/$', SneakersColorsSizesRelSearch.as_view({'get': 'list'}), name='search')

]
