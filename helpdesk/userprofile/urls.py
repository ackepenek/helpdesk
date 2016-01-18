'''
Created on Jan 16, 2016

@author: ahmetcan
'''
from django.conf.urls import include, url
from django.contrib import admin

from userprofile.views import login, logout, create_profile, update_profile


urlpatterns = [
    url(r'^login/$', login, name = "login"),
    url(r'^logout/$', logout, name = "logout"),
    url(r'^profile/create$', create_profile, name = "create_profile"),
    url(r'^profile/update$', update_profile, name = "update_profile"),
]