# -*- coding:utf-8 -*-

from django.contrib import admin

from ticketsystem.models import Product, Status, Priority, Ticket


class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class StatusAdmin(admin.ModelAdmin):
    pass
admin.site.register(Status, StatusAdmin)

class TicketAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ticket, TicketAdmin)
