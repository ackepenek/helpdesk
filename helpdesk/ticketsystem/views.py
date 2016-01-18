# -*- coding:utf-8 -*-
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from ticketsystem.forms import CreateTicketForm, UpdateTicketForm, FollowUpForm
from ticketsystem.models import FollowUp, Ticket


@login_required
def create_ticket(request):
    data = {}
    if request.POST:
        form = CreateTicketForm(request.POST)
        
        if form.is_valid():
            try:
                ticket = form.instance
                ticket.department = request.user.userprofile.department
                ticket.creator = request.user.userprofile
                ticket.save()
                follow_up = FollowUp()
                follow_up.ticket = ticket
                follow_up.assigned_user = request.user.userprofile
                follow_up.followup_date = ticket.created_date
                follow_up.followup_user = request.user.userprofile
                follow_up.save()
                return HttpResponseRedirect(reverse("ticket_detail") + "?ticket_id=" + ticket.id) 
            except Exception as e:
                print e.message
                note = "Hata Oluştu"
                return HttpResponseRedirect(reverse("index"))
        else:
            note = "Form Kaydedilemedi"
    else:
        note = "Yeni İş Oluştur"
        form = CreateTicketForm()
    data['form'] = form
    data['note'] = note
    return render(request, "create_ticket.html", data)
    
@login_required
def ticket_detail(request, ticket_id):
    data = {}
    if request.POST:
        try:
            update_ticket_form = UpdateTicketForm(request.POST, 
                                                    prefix='update_ticket_form', 
                                                    instance=Ticket.objects.get(id = ticket_id))
            try:
                followup_form = FollowUpForm(request.POST,
                                                    prefix='followup_form',
                                                    instance=FollowUp.objects.get(ticket=Ticket.objects.get(id = ticket_id)))
            except ObjectDoesNotExist:
                followup_form = FollowUpForm(request.POST,
                                                    prefix='followup_form')
            if all([update_ticket_form.is_valid(), followup_form.is_valid()]):
                ticket = update_ticket_form.save()
                followup = followup_form.save(commit=False)
                followup.ticket = ticket
                followup.followup_user = request.user.userprofile
                followup.followup_date = datetime.now()
                followup.save()
        except:
            return HttpResponseRedirect(reverse("index"))
    else:
        try:
            update_ticket_form = UpdateTicketForm(prefix='update_ticket_form', 
                                                    instance=Ticket.objects.get(id = ticket_id))
            print ticket_id
            try:
                followup_form = FollowUpForm(prefix='followup_form',
                                                    instance=FollowUp.objects.get(ticket=Ticket.objects.get(id = ticket_id)))
            except ObjectDoesNotExist:
                followup_form = FollowUpForm(prefix='followup_form')

            
        except Exception as e:
            print e.message
            return HttpResponseRedirect(reverse("index"))
    data['update_ticket_form'] = update_ticket_form
    data['followup_form'] = followup_form
    return render(request, "ticket_detail.html", data)

@login_required
def ticket_list(request):
    data = {}
    try:
        ticket_list = Ticket.objects.filter(department=request.user.userprofile.department)
        data['ticket_list'] = ticket_list
        return render(request, "ticket_list.html", data)
    except Exception as e:
        print e.message
        return HttpResponseRedirect(reverse("index"))
