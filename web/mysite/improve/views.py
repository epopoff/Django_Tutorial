from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Ticket, Category

# Create your views here.
# def ticket_list(request):
# 	tickets = Ticket.objects.order_by('created_date')
# 	return render(request, 'improve/ticket_list.html', {'tickets' : tickets})


class TicketList(generic.ListView):
    template_name = 'improve/ticket_list.html'
    context_object_name = 'latest_tickets_list'

    def get_queryset(self):
        return Ticket.objects.order_by('-created_date')[:10]
