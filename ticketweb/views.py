from django.shortcuts import render,redirect
from tickets.models import Event, Ticket

def index(request):
    user = request.user
    events = Event.objects.all()
    tickets = Ticket.objects.all()
    context = {"user":user,
               "events":events,
               "tickets": tickets
            }
    print(tickets)
    if not user.is_active:
        return redirect('log_in')
    return render(request, 'index.html', context)

def ticket_details(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    context ={
        "ticket":ticket
    }
    return render(request, 'ticket_detail.html', context)