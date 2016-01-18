# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from django.forms.widgets import TextInput

from userprofile.models import UserProfile


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        widgets = {
                    'first_name': forms.TextInput(attrs={'placeholder': 'Ad', 'class':'form-control'}),
                    'last_name': forms.TextInput(attrs={'placeholder': 'Soyad', 'class':'form-control'}),
                    'email': forms.TextInput(attrs={'placeholder': 'E-posta', 'class':'form-control'}),
                    'username': forms.TextInput(attrs={'readonly':'readonly', 'class':'form-control'})
                  }
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = {}
        fields = ['gender', 'title', 'department', 'profile_photo']
        
        widgets={                    
            'gender' : forms.Select(attrs={'placeholder': 'Cinsiyet', 'class':'form-control'}),
            'title' : forms.TextInput(attrs={'placeholder':'Ünvan', 'class':'form-control'}),
            'department': forms.Select(attrs={'class':'form-control'})
        }        
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
