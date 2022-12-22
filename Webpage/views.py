from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import login, authenticate, logout
from Webpage.forms import UserRegister, UserLogin, CreateTicketForm
from tickets.models import Ticket




def home_page(request):
    # if request.user.is_authenticated:
    #     return render(request, "dashboard.html")
    # else:
    return render(request, "home.html")

def user_register(request):
    form = UserRegister()
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            # Where you want to go after a successful signup
            return redirect("home_page")
    context = {
        "form": form,
    }
    return render(request, "register.html", context)

def user_login(request):
    form = UserLogin()
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                # Where you want to go after a successful login
                return redirect("home_page")

    context = {
        "form": form,
    }
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect("home_page")

def ticket_add(request):
    tickets = Ticket.objects.all()
    
    context = {
        'tickets': tickets
    }
    return render(request, "Ticket_add.html", context)

def create_ticket(request):
    form = CreateTicketForm()
    if request.method == "POST":

        form_D = CreateTicketForm(request.POST, request.FILES)
        
        if form_D.is_valid():
            
            form_D.save()
            
            return redirect("tickts_page")
    context = {
        "form": form
    }
    return render(request, "dashboard.html", context)

def prfile_page(request):
    context={
        "user":request.user,
        "tickets":request.user.owned_tickets.all()
    }

    return render(request, 'profile.html', context)

def ticket_view(request):
    return render(request, "Ticket_view.html")


def ticket_item(request, ticket_id):
    try:
        ticket = Ticket.objects.get(id=ticket_id)
        # store_item = models.StoreItem.objects.get(id=item_id)
    except Ticket.DoesNotExist:
        raise Http404("item does not exist")

    ticket.delete()
    return redirect("profile_page")