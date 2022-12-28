from django.shortcuts import render,redirect
from tickets.models import Event, Ticket

cart = []
def index(request):
    user = request.user
    events = Event.objects.all()
    tickets = Ticket.objects.filter(available = True)
    context = {"user":user,
               "events":events,
               "tickets": tickets,
                "cart_counter": len(cart),
                "cart": cart
            }
    print(tickets)
    if not user.is_active:
        return redirect('log_in')
    return render(request, 'index.html', context)

def ticket_details(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    context ={
        "ticket":ticket,
        "cart_counter": len(cart),
        "cart": cart,
        "ticket_in_cart": ticket.id not in [a_cart.id for a_cart in cart]
        
    }
    return render(request, 'ticket_detail.html', context)

def add_to_cart(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if (ticket.available):
        if ticket.id not in [a_cart.id for a_cart in cart]:
            cart.append(ticket)
        # ticket.owner = request.user
        # ticket.available = False
        # ticket.save()
    return redirect('index')
    

def my_cart(request):
    context={
        "cart_counter": len(cart),
        "cart": cart,
        "total": sum([ticket.price for ticket in cart])
    }
    return render(request, 'cart.html', context)

def remove_ticket_from_cart(request, ticket_id):
    print(cart)
    for index,ticket in enumerate(cart):
        if ticket.id == ticket_id:
            the_index = index
    cart.pop(the_index)
    return redirect('my_cart')

def buy_the_cart(request):
    for ticket in (cart):
        ticket.owner = request.user
        ticket.available = False
        ticket.save()
    for ticket in cart:
        cart.pop()
    if(cart):
        cart.pop()
    return redirect('my_cart')


def profile(request):
    user = request.user
    context={
        "user":user,
        "tickets":user.owned_tickets.all(),
    }
    return render(request, 'profile.html', context)

def add_new_ticket(request):
    context={}
    return render(request, 'addTicket.html', context)
