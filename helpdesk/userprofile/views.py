# -*- coding:utf-8 -*-

import user

from django.contrib.auth import authenticate, logout as user_logout, login as user_login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.forms.formsets import formset_factory
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt

from userprofile.forms import UserProfileForm, UserForm
from userprofile.models import UserProfile


@csrf_exempt
def login(request):
    data = {}
    note = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            user_login(request, user)
            return HttpResponseRedirect(reverse("index"))
        note = "Giriş Başarısız"
    data['note'] = note
    return render_to_response("login.html", data)

def logout(request):
    user_logout(request)
    return HttpResponseRedirect(reverse("login"))

@login_required
def create_profile(request):
    if request.POST:
        userprofile_form = UserProfileForm(request.POST, request.FILES, prefix='userprofile_form')
        user_form = UserForm(request.POST, request.FILES, prefix='user_form')
        if all([userprofile_form.is_valid(), user_form.is_valid()]):
            user = user_form.save()
            profile = userprofile_form.save(commit=False)
            profile.user = user
            profile.save()
    else:
        userprofile_form = UserProfileForm(prefix='userprofile_form')
        user_form = UserForm(prefix='user_form') 
    return render(request, "user_profile.html", {
        'userprofile_form': userprofile_form,
        'user_form': user_form
    })

@login_required
def update_profile(request):
    data = {}
    if request.POST:
        try:
            userprofile_form = UserProfileForm(request.POST, request.FILES, prefix='userprofile_form', instance=request.user.userprofile)
        except ObjectDoesNotExist:
            userprofile_form = UserProfileForm(request.POST, request.FILES, prefix='userprofile_form')
        user_form = UserForm(request.POST, request.FILES, prefix='user_form', instance=request.user)
        if all([userprofile_form.is_valid(), user_form.is_valid()]):
            user = user_form.save()
            profile = userprofile_form.save(commit=False)
            profile.user = user
            print userprofile_form
            profile.save()
            return redirect("update_profile")
    else:
        user_form = UserForm(instance=request.user, prefix='user_form')
        try:
            userprofile_form = UserProfileForm(prefix='userprofile_form', instance=request.user.userprofile)
        except ObjectDoesNotExist:
            userprofile_form = UserProfileForm(prefix='userprofile_form')
    data['userprofile_form'] = userprofile_form
    data['user_form'] = user_form
    return render(request, "user_profile.html", data)
