# -*- coding: utf-8 -*-

import os

from django.contrib.auth.models import User
from django.db import models

from django.conf import settings

class Department(models.Model):
    name = models.CharField(verbose_name="Bölüm", max_length="11")
    depadmin = models.ForeignKey(User)
    def __unicode__(self):
        return self.name

def get_image_path(instance, filename):
    return os.path.join(settings.MEDIA_URL, 'images', str(instance.user.id), filename)

class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('K', 'Kadın'),
        ('E', 'Erkek'),
    )
    user = models.OneToOneField(User)
    gender = models.CharField(choices=GENDER_CHOICES, verbose_name="Cinsiyet", max_length=1)
    title = models.CharField(verbose_name="Ünvan", max_length=40)
    department = models.ForeignKey(Department) 
    profile_photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    def __unicode__(self):
        return self.user.username
    def get_image_relative_path(self):
        print self.profile_photo.path
        print self.profile_photo.url
        return os.path.join('static', 'images', str(self.user.id), self.profile_photo.name)
