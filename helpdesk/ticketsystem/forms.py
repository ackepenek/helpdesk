# -*- coding: utf-8 -*-

from django import forms
from django.forms.models import ModelForm

from ticketsystem.models import Ticket, FollowUp


class CreateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude = {}
        fields = ['title', 'description', 'product', 'priority', 'status']
        
        widgets={                    
            'title' : forms.TextInput(attrs={'placeholder':'Başlık', 'class':'form-control'}),
            'description' : forms.Textarea(attrs={'placeholder':'Açıklama', 'class':'form-control'}),
            'product' : forms.Select(attrs={'placeholder':'Ürün', 'class':'form-control'}),
            'priority' : forms.Select(attrs={'placeholder':'Öncelik', 'class':'form-control'}),
            'status' : forms.Select(attrs={'placeholder':'Durum', 'class':'form-control'}),
        }
        help_texts = {
            'title': "Yapılacak işin özet olarak başlık bilgisini içerir",
            'description' : "Yapılacak işin detaylarını içerir",
            'product' : "Yapılacak işin ilişkili olduğu ürün bilgisidir",
            'priority': "Yapılacak işin öncelik bilgisidir",
            'status' : "Yapılacak işin durumunu belirtir"
        } 
        
    def __init__(self, *args, **kwargs):
        super(CreateTicketForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
            

class UpdateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude = {}
        fields = ['id', 'title', 'description', 'product', 'priority', 'status']
        
        widgets={
            'id' : forms.TextInput(attrs={'readonly':'readonly', 'placeholder':'İş No', 'class':'form-control'}),                    
            'title' : forms.TextInput(attrs={'placeholder':'Başlık', 'class':'form-control'}),
            'description' : forms.Textarea(attrs={'placeholder':'Açıklama', 'class':'form-control'}),
            'product' : forms.Select(attrs={'placeholder':'Ürün', 'class':'form-control'}),
            'priority' : forms.Select(attrs={'placeholder':'Öncelik', 'class':'form-control'}),
            'status' : forms.Select(attrs={'placeholder':'Durum', 'class':'form-control'}),
        }
        help_texts = {
            'title': "Yapılacak işin özet olarak başlık bilgisini içerir",
            'description' : "Yapılacak işin detaylarını içerir",
            'product' : "Yapılacak işin ilişkili olduğu ürün bilgisidir",
            'priority': "Yapılacak işin öncelik bilgisidir",
            'status' : "Yapılacak işin durumunu belirtir"
        } 
        
    def __init__(self, *args, **kwargs):
        super(UpdateTicketForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
            


class FollowUpForm(ModelForm):
    class Meta:
        model = FollowUp
        exclude = {}
        fields = ['followupnote', 'followup_user', 'assigned_user']
        
        widgets={                    
            'followupnote' : forms.TextInput(attrs={'placeholder':'Not', 'class':'form-control'}),
            'followup_user' : forms.Select(attrs={'readonly':'readonly', 'placeholder':'Yorumlayan', 'class':'form-control'}),
            'assigned_user' : forms.Select(attrs={'placeholder':'Atanan', 'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(FollowUpForm, self).__init__(*args, **kwargs)