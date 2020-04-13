"""silentcombat URL Configuration

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
from django.contrib import admin
from django.urls import path

from index.views import *
from news.views import posts

urlpatterns = [
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
#    path('gallery/', gallery_view, name='gallery'),
    path('news/', posts, name='news'),
#    path('contact/', contact_view, name='contact'),
    path('rules/', rules_view, name='rules'),
#    path('servers/', servers_view, name='servers'),
    path('donate/', donate_view, name='donate'),
    path('admin/', admin.site.urls),
]
