from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

@login_required   
def protected_view(request):
    return render(request, 'home/about.html') 

class CustomLoginView(LoginView):
    template_name = 'templates/login.html'   

def hero(request):
    return render(request, 'hero.html') 

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "login.html")

def signup_views(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        Pass1 = request.POST['Pass1']
        Pass2 = request.POST['Pass2']

        # Create the user
        try:
            # Use create_user to set the username, email, and password
            myuser = User.objects.create_user(username=username, email=email, password=Pass1)
            # Set the first and last name
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            
            messages.success(request, "Your account has been successfully created.")
            return redirect('login')

        except IntegrityError as e:
            return render(request, 'signup.html', {'error_message': 'Error creating user'})

    return render(request, 'signup.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("hero"))

 