from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                username=username,
                password=password
            )

            if user:

                login(request, user)

                return redirect("dashboard")

            else:

                form.add_error(None, "Invalid Username or Password")

    return render(
        request,
        "accounts/login.html",
        {
            "form": form
        }
    )


def logout_view(request):

    logout(request)

    return redirect("login")

