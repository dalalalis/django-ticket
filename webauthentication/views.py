from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import UserRegister, UserLogin

# Create your views here.
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
            return redirect("index")
    context = {
        "form": form,
    }
    return render(request, "register.html", context)

def user_login(request):
    form = UserLogin()
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():
            print('valid')
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print(username)
            print(password)
            auth_user = authenticate(username=username, password=password)
            print(auth_user)
            if auth_user is not None:
                print('here')
                login(request, auth_user)
                # Where you want to go after a successful login
                return redirect("index")

    context = {
        "form": form,
    }
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect("index")