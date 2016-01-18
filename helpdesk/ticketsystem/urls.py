'''
Created on Jan 16, 2016

@author: ahmetcan
'''
from django.conf.urls import include, url
from django.contrib import admin

from ticketsystem.views import ticket_detail, create_ticket, ticket_list


urlpatterns = [
    url(r'^show/$', ticket_detail, name = "ticket_detail"),
    url(r'^create/$', create_ticket, name = "create_ticket"),
    url(r'^list/$', ticket_list, name = "ticket_list"),
    url(r'^detail/(?P<ticket_id>[0-9]+)/$', ticket_detail, name="ticket_detail"),
]