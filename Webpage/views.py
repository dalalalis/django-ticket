from django.shortcuts import render, redirect
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
    Ticketss = Ticket.objects.all()
    context = {
        'tickets': Ticketss
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
    return render(request, 'profile.html')


def ticket_view(request):
    # if request.user.is_authenticated:
    #     return render(request, "dashboard.html")
    # else:
    return render(request, "Ticket_view.html")