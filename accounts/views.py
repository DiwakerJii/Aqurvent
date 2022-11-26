from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def home(request):
    return render(request, "/home.html")


def register(request):
    
    if request.method == "POST":

        username = request.POST.get('username', None)
        name = request.POST.get('name', None)
        email= request.POST.get('email', None)
        pass1 = request.POST.get('pass1', None)

        myuser = User.objects.created_user(username, email, pass1 )
        myuser.name = name

        myuser.save()
        messages.success(request, "Your Account has been successfully created. ")

        return redirect('login')




def login(request):
    return render(request, "login.html")
        