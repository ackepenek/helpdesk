'''
Created on Jan 16, 2016

@author: ahmetcan
'''
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render


def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse("login"))
        
    else:
        return render(request, "index.html")
