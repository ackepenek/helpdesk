# -*- coding:utf-8 -*-
from ticketsystem.models import Ticket


def tickets(request):
    try:
        assigned_tickets = Ticket.objects.filter(followup__assigned_user=request.user.userprofile)
    except:
        assigned_tickets = []
    return {'assigned_tickets': assigned_tickets}
    

