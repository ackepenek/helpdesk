# -*- coding:utf-8 -*-

from datetime import datetime

from django.db import models

from userprofile.models import Department, UserProfile


class Product(models.Model):
    name = models.CharField(verbose_name="Product", max_length = 50)
    department = models.ForeignKey(Department)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

class Status(models.Model):
    name = models.CharField(verbose_name="Status", max_length="15")
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statutes"
        
class Priority(models.Model):
    name= models.CharField(verbose_name="Priority", max_length="15")
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = "Priority"
        verbose_name_plural = "Priorities"

class Ticket(models.Model):
    product = models.ForeignKey(Product, verbose_name="Ürün")
    department = models.ForeignKey(Department, verbose_name="Bölüm")
    status = models.ForeignKey(Status, verbose_name="Durum")
    priority = models.ForeignKey(Priority, verbose_name="Öncelik")
    creator = models.ForeignKey(UserProfile, verbose_name="Oluşturan")
    title = models.CharField(verbose_name="Başlık", max_length = 100)
    description = models.CharField(verbose_name="Açıklama", max_length = 1000)
    created_date = models.DateTimeField(verbose_name="Oluşturma Tarihi", default=datetime.now)
    def __unicode__(self):
        return self.title
 
class FollowUp(models.Model):
    ticket = models.ForeignKey(Ticket)
    followupnote = models.CharField(verbose_name="Yorum", max_length = 1000)
    followup_date = models.DateTimeField(verbose_name="Güncelleme Tarihi", blank=True, null=True)
    followup_user = models.ForeignKey(UserProfile, related_name='followup_user', verbose_name="Yorumlayan")
    assigned_user = models.ForeignKey(UserProfile, related_name='assigned_user', verbose_name="Atanan")
