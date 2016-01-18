"""helpdesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url, static
from django.contrib import admin

from helpdesk.views import index


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('userprofile.urls')),
    url(r'^ticket/', include('ticketsystem.urls')),
    url(r'^$', index, name="index"),
]

if settings.DEBUG is True:
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

