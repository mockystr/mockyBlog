from django.shortcuts import render, redirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm


def login(request):
    args = {}
    args.update(csrf(request))

    if request.POST:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            args["login_error"] = "User is not found"
            return render(request, "login.html", args)
    else:
        return render(request, "login.html", args)


def logout(request):
    auth.logout(request)
    return redirect("/auth/login")


def register(request):
    args = {}
    args.update(csrf(request))
    args["form"] = UserCreationForm()

    if request.POST:
        new_user_form = UserCreationForm(request.POST)

        if new_user_form.is_valid():
            new_user_form.save()
            new_user = auth.authenticate(username=request.POST.get("username", ""),
                                         password=request.POST.get("password1", ""))
            auth.login(request, new_user)
            return redirect("/")
        else:
            args["form"] = new_user_form
    return render(request, "register.html", args)
